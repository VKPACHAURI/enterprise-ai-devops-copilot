# Phase 3 Debugging Notes

## Issue

While running unit tests, pytest reported:

ModuleNotFoundError:
No module named 'utils'
No module named 'config'

---

## Root Cause

The project structure was correct.

The issue occurred because the tests were executed using:

pytest -v

instead of

python -m pytest -v

---

## Resolution

Executed the test suite using:

python -m pytest -v

Python correctly resolved the project modules.

---

## Result

23/23 Tests Passed Successfully.

---

## Learning

Always execute pytest using:

python -m pytest

This guarantees that the active Python interpreter and virtual environment are used consistently.