# Phase 2 - Enterprise Logging Debugging Notes

## Issue 1 - ModuleNotFoundError: No module named 'utils'

### Error

ModuleNotFoundError: No module named 'utils'

### Root Cause

The application was executed using:

python app/main.py

When Python executes a file directly, it changes the module search path and cannot correctly resolve sibling packages.

### Solution

Run the application as a module:

python -m app.main

### Learning

Enterprise Python applications should be executed as modules instead of running individual files directly.

---

## Issue 2 - ImportError: cannot import name 'BASE_DIR'

### Error

ImportError: cannot import name 'BASE_DIR'

### Root Cause

BASE_DIR was defined inside the Settings class.

The code incorrectly imported:

from config.settings import BASE_DIR

instead of accessing it through the settings instance.

### Solution

Use:

from config.settings import settings

Then:

settings.BASE_DIR

### Learning

Understand the difference between module-level variables and class attributes.

---

## Issue 3 - Logger Handlers Duplicated

### Problem

Calling get_logger() multiple times created duplicate console and file handlers.

This caused repeated log messages.

### Root Cause

Handlers were added every time get_logger() was called.

### Solution

Prevent duplicate handlers using:

if not logger.handlers:

### Learning

Python's logging module returns the same logger instance for the same logger name.

Always check existing handlers before adding new ones.

---

## Issue 4 - Log Directory Missing

### Problem

The logs directory did not exist on a fresh project setup.

### Solution

Automatically create the directory:

LOG_DIR.mkdir(parents=True, exist_ok=True)

### Learning

Applications should prepare their runtime environment automatically instead of requiring manual setup.

---

## Issue 5 - Logger Validation

### Problem

The logger implementation needed verification beyond manual testing.

### Solution

Implemented six unit tests to validate:

- Logger instance
- Logger name
- Logger level
- Duplicate handler prevention
- Log directory creation
- Log file creation

### Learning

Unit tests verify behavior automatically and prevent regressions when the code evolves.
