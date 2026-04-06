#!/usr/bin/env python3
"""
Validates GitHub Actions workflow YAML templates for structural correctness.
Checks: YAML syntax, required fields, actions versions, best practices.
"""
import yaml
import glob
import sys
import os

errors = 0
warnings = 0

def error(msg):
    global errors
    print(f"  ❌ {msg}")
    errors += 1

def warn(msg):
    global warnings
    print(f"  ⚠️  {msg}")
    warnings += 1

def ok(msg):
    print(f"  ✅ {msg}")

print("Validating CI pipeline templates...\n")

templates = sorted(glob.glob("workflows/**/*.yml", recursive=True))
print(f"Found {len(templates)} template(s)\n")

for filepath in templates:
    print(f"  {filepath}:")

    # 1. YAML syntax
    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        error(f"Invalid YAML: {e}")
        continue

    if not isinstance(data, dict):
        error("Root must be a mapping")
        continue

    # 2. Required top-level fields
    if "name" not in data:
        warn("Missing 'name' field")

    # PyYAML parses 'on' as boolean True, so check for both
    if "on" not in data and True not in data:
        error("Missing 'on' trigger")

    if "jobs" not in data:
        error("Missing 'jobs' section")
        continue

    # 3. Check permissions (least privilege)
    if "permissions" not in data:
        warn("No 'permissions' block — consider adding for least-privilege")

    # 4. Validate each job
    for job_name, job in data.get("jobs", {}).items():
        if not isinstance(job, dict):
            error(f"Job '{job_name}' is not a mapping")
            continue

        if "runs-on" not in job:
            error(f"Job '{job_name}' missing 'runs-on'")

        steps = job.get("steps", [])
        if not steps:
            error(f"Job '{job_name}' has no steps")
            continue

        # Check for checkout action
        has_checkout = any(
            s.get("uses", "").startswith("actions/checkout")
            for s in steps if isinstance(s, dict)
        )
        if not has_checkout:
            warn(f"Job '{job_name}' doesn't check out code")

        # Check actions versions (should use @v4, not @v6/v7 which don't exist)
        for step in steps:
            if not isinstance(step, dict):
                continue
            uses = step.get("uses", "")
            if uses:
                # Warn on deprecated @v3 or lower
                for action in ["actions/checkout", "actions/setup-node", "actions/upload-artifact"]:
                    if uses.startswith(action) and "@v" in uses:
                        version = uses.split("@v")[-1]
                        try:
                            v = int(version)
                            if v < 4:
                                warn(f"'{uses}' — consider upgrading to @v4")
                            elif v > 4:
                                error(f"'{uses}' — v{v} does not exist, use @v4")
                        except ValueError:
                            pass

    ok("Valid")

print(f"\nValidated {len(templates)} templates: {errors} error(s), {warnings} warning(s)")

if errors > 0:
    print("❌ Validation failed")
    sys.exit(1)
else:
    print("✅ All templates valid")
