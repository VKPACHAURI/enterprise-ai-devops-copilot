# Debugging Report 001

## Date

2026-07-15

## Module

config/constants.py

## Problem

ModuleNotFoundError: No module named 'config'

## Symptoms

Python could not import the config package.

## Root Cause

The test was executed directly using:

python tests/test_constants.py

This caused Python to use the tests directory as the module search path.

## Solution

Run tests using:

python -m pytest tests/

instead of:

python tests/test_constants.py

## Lessons Learned

- Never execute test files directly in package-based projects.
- Always use pytest.
- Understand Python module search paths.

## Prevention

Use pytest consistently for all future tests.

## Status

Resolved ✅




