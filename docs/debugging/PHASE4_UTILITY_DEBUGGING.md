# Phase 4 – Enterprise File Utility Framework

## Debugging Notes

---

# Objective

Develop a reusable Enterprise File Utility Framework that provides standardized file and directory operations with enterprise-grade logging, exception handling, and unit testing.

---

# Issue 1 – Import Error During Unit Testing

## Error

```text
ModuleNotFoundError: No module named 'utils'
```

or

```text
ModuleNotFoundError: No module named 'utils.file_utility'
```

---

## Root Cause

Pytest was unable to import the project module because the project structure or import path was incorrect.

---

## Resolution

* Verified the project structure.
* Confirmed the location of `file_utility.py`.
* Corrected the import path.
* Re-ran the test suite successfully.

---

## Lesson Learned

Always verify the project structure before modifying application code.

Most import errors are caused by:

* Incorrect package structure
* Incorrect module names
* Incorrect import statements

---

# Issue 2 – Exception Test Failed

## Error

```text
Failed: DID NOT RAISE FileOperationError
```

---

## Root Cause

The test used:

```python
FileUtility.create_directory("logs")
```

The `logs` directory already existed.

Because of this, the method returned early:

```python
if path.exists() and path.is_dir():
    return
```

The execution never reached:

```python
path.mkdir(...)
```

Therefore, the monkeypatched `mkdir()` method was never called.

---

## Resolution

Used a fresh temporary directory created by the `tmp_path` pytest fixture.

This guaranteed that:

* The directory did not already exist.
* `path.mkdir()` was executed.
* The monkeypatched method raised `PermissionError`.
* The application correctly raised `FileOperationError`.

---

## Lesson Learned

When writing unit tests, always verify that the execution reaches the code being tested.

A correctly configured mock is ineffective if the application returns before reaching the mocked method.

---

# Testing Techniques Used

## tmp_path

Purpose:

* Creates an isolated temporary directory.
* Prevents modification of the real filesystem.
* Automatically cleans up after the test.

---

## monkeypatch

Purpose:

* Temporarily replaces methods or objects.
* Simulates failure scenarios.
* Avoids changing the real operating system or filesystem.

---

## pytest.raises()

Purpose:

Verify that the expected custom exception is raised.

Example:

```python
with pytest.raises(FileOperationError):
    ...
```

---

# Enterprise Concepts Reinforced

During this phase the following concepts were practiced:

* Utility Class Design
* DRY Principle
* Reusability
* Defensive Programming
* Structured Logging
* Exception Chaining
* Custom Exceptions
* Modern Path Handling (`pathlib`)
* Unit Testing
* Mocking
* Test Isolation

---

# Commands Used

Run Phase 4 tests:

```bash
pytest tests/test_file_utility.py -v
```

Run the complete project test suite:

```bash
pytest -v
```

---

# Key Takeaways

* Centralize reusable file-system operations.
* Avoid duplicate code across modules.
* Standardize logging and exception handling.
* Validate both success and failure scenarios.
* Build isolated and repeatable unit tests.
* Use debugging logs to identify execution paths.
* Analyze root causes before applying fixes.

---

# Phase 4 Summary

**Completed Successfully**

Deliverables:

* ✔ Enterprise File Utility Framework
* ✔ create_directory() implementation
* ✔ Unit Test Suite
* ✔ Enterprise Documentation
* ✔ Interview Notes
* ✔ Debugging Notes

The project now has a reusable foundation for all future file and directory operations, which will be leveraged by the Document Loader, Vector Store, and RAG Pipeline in the upcoming phases.
