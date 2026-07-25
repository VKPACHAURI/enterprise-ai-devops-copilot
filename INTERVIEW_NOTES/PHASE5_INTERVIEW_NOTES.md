# PHASE 5 INTERVIEW NOTES

Project: Enterprise AI DevOps Copilot

Phase: Enterprise Document Loader Framework

Author: Vishesh Pachauri

---

# 1. What is a Document Loader?

Answer:

A Document Loader is responsible for reading documents from a storage location
and converting them into objects that can be processed by downstream AI
components such as text splitters, embedding models, and vector databases.

---

# 2. Why did you create a separate DocumentLoader class?

Answer:

To follow the Single Responsibility Principle.

The DocumentLoader is responsible only for:

- Validating directories
- Discovering supported files
- Loading documents
- Logging
- Exception handling

It does not perform text splitting, embedding generation, retrieval, or AI
inference.

---

# 3. Why didn't you hardcode the document path?

Answer:

Hardcoding paths makes applications difficult to maintain.

Instead, the directory path is provided by the caller, making the component
reusable across development, testing, and production environments.

---

# 4. Why did you use pathlib instead of os.path?

Answer:

Pathlib provides an object-oriented API for filesystem operations.

Advantages include:

- Better readability
- Cross-platform compatibility
- Cleaner syntax
- Recommended in modern Python

---

# 5. Difference between exists(), is_file(), and is_dir()?

Answer:

exists()

Checks whether a filesystem object exists.

It returns True for both files and directories.

is_file()

Returns True only if the path is a file.

is_dir()

Returns True only if the path is a directory.

---

# 6. Why did you validate the directory before loading files?

Answer:

Validation prevents runtime failures.

Instead of allowing Python to throw unexpected exceptions later, the framework
fails early with meaningful custom exceptions.

---

# 7. Why did you filter supported file types?

Answer:

To prevent unsupported documents from entering the AI pipeline.

This avoids unnecessary processing and reduces the chance of runtime errors.

---

# 8. Why did you use a set for supported file types?

Answer:

Sets provide very fast membership lookup.

Example:

".pdf" in self.supported_file_types

This operation is efficient and easy to extend.

---

# 9. Why did you use suffix.lower()?

Answer:

Users may upload files like:

AWS.PDF

aws.PDF

Aws.Pdf

Converting the extension to lowercase makes file matching
case-insensitive.

---

# 10. Why did you use PyPDFLoader?

Answer:

PyPDFLoader is a LangChain document loader that converts PDF files into
Document objects suitable for downstream AI processing.

---

# 11. What does PyPDFLoader return?

Answer:

It returns a list of LangChain Document objects.

Each Document contains:

- page_content
- metadata

---

# 12. Why didn't you use print()?

Answer:

Production applications use centralized logging because logs can be stored,
searched, monitored, and analyzed.

print() is suitable only for quick debugging.

---

# 13. Why did you use custom exceptions?

Answer:

Custom exceptions make failures easier to understand and allow callers to
handle specific application errors without relying on generic Python
exceptions.

---

# 14. Why did you use exception chaining?

Answer:

Using:

raise ... from error

preserves the original exception while providing a business-specific exception.

This improves debugging.

---

# 15. Why did you re-raise DocumentLoadError?

Answer:

To avoid wrapping the same exception multiple times.

Already handled business exceptions should propagate unchanged.

---

# 16. Why did you write unit tests?

Answer:

Unit tests verify that each function behaves correctly in both success and
failure scenarios.

They reduce regressions during future development.

---

# 17. Why did you use tmp_path?

Answer:

tmp_path creates temporary directories and files that are automatically cleaned
up after the test.

This keeps tests isolated and repeatable.

---

# 18. Why did you use monkeypatch?

Answer:

monkeypatch replaces external dependencies during testing.

This allows unit tests to verify only our own code without depending on
external libraries.

---

# 19. Why mock PyPDFLoader?

Answer:

Unit tests should test our application logic, not LangChain itself.

Mocking keeps tests fast, deterministic, and independent of real PDF files.

---

# 20. What happens after the Document Loader?

Answer:

The loaded LangChain Documents are passed to the Text Splitter, which divides
them into smaller chunks before embedding generation.

---

# Phase 5 Architecture

Application

↓

DocumentLoader

↓

Directory Validation

↓

Supported File Discovery

↓

PyPDFLoader

↓

LangChain Documents

↓

Text Splitter

---

# Unit Test Summary

✔ Initialization

✔ Directory Not Found

✔ Invalid Directory Path

✔ Unsupported Files

✔ Successful PDF Loading

✔ PDF Loading Failure

Total Tests: 6 / 6 Passed

---

# Key Learnings

- Enterprise document loading
- Directory validation
- File filtering
- LangChain document loading
- Logging integration
- Custom exception handling
- Unit testing with pytest
- Mocking using monkeypatch
- Temporary filesystem testing using tmp_path

---

# Interview Summary

In this phase, I designed and implemented a reusable Enterprise Document Loader
Framework that follows enterprise software engineering principles. The solution
provides centralized document loading, validation, structured logging, custom
exception handling, and comprehensive unit testing. It forms the foundation for
the next stage of the RAG pipeline, where documents will be split into chunks
before generating embeddings.