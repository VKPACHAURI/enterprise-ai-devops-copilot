# Enterprise AI DevOps Copilot

An enterprise-grade AI-powered DevOps Copilot built with Python, LangGraph, Ollama, and ChromaDB.

## 🚀 Project Goal

Build a production-style AI platform capable of:

- Multi-Agent AI
- Agentic AI workflows
- DevOps automation
- Retrieval-Augmented Generation (RAG)
- Local LLM execution using Ollama
- Docker
- Kubernetes
- Terraform
- AWS deployment

## Technology Stack

- Python
- LangGraph
- LangChain
- Ollama
- ChromaDB
- Docker
- Kubernetes
- Terraform
- AWS

## Project Status

🚧 Under Development
i## Completed Features

### Phase 1 – Enterprise Foundation

- Enterprise project initialization
- Modular project structure
- Runtime configuration management
- Application constants management
- Python virtual environment
- Unit testing with pytest
- GitHub repository initialization
- WSL2 Ubuntu development environment
- Enterprise documentation

---
### Pahse 2
## Features

- Enterprise Project Structure
- Centralized Runtime Configuration
- Application Constants Module
- Enterprise Logging Framework
- Console Logging
- File Logging
- Structured Log Formatting
- Automatic Log Directory Creation
- Duplicate Handler Prevention
- Unit Testing with Pytest
- Modular Architecture (SRP)
- Enterprise Documentation


### Phase 3

- Enterprise Exception Framework
- Centralized Custom Exceptions
- Reusable Base Exception
- Exception Unit Tests
- Enterprise Error Hierarchy


 **Phase 4 – Enterprise File Utility Framework**

  * Developed a reusable `FileUtility` class for enterprise file and directory management.
  * Implemented standardized directory creation using `pathlib.Path`.
  * Centralized file operation logging.
  * Integrated custom exception handling using `FileOperationError`.
  * Added comprehensive unit tests covering:

    * Successful directory creation
    * Existing directory handling
    * Exception handling
  * Eliminated duplicate file-system logic across modules by introducing reusable utilities.

---

### Current Project Status

* ✅ Project Structure
* ✅ Configuration Framework
* ✅ Logging Framework
* ✅ Exception Framework
* ✅ Enterprise File Utility Framework

**Status:** Ready for Phase 5
# Phase 5: Enterprise Document Loader Framework

## Overview

The Enterprise Document Loader Framework is responsible for discovering,
validating, and loading supported documents into the Enterprise AI DevOps
Copilot.

This framework provides a centralized implementation for document loading,
ensuring enterprise-level validation, structured logging, and custom
exception handling.

---

## Features

- Supports loading PDF documents.
- Validates that the provided path exists.
- Ensures the supplied path is a directory.
- Automatically discovers supported document types.
- Prevents processing unsupported files.
- Raises custom enterprise exceptions.
- Provides centralized logging for every loading operation.
- Returns LangChain document objects for downstream processing.

---

## Architecture

```
Application
      │
      ▼
DocumentLoader
      │
      ▼
Validate Directory
      │
      ▼
Discover Supported Files
      │
      ▼
Load PDF Documents
      │
      ▼
Return LangChain Documents
```

---

## Supported File Types

| Extension | Status |
|-----------|--------|
| .pdf | Supported |

---

## Enterprise Benefits

- Single Responsibility Principle (SRP)
- Centralized document loading
- Reusable framework
- Enterprise logging
- Enterprise exception handling
- Easy to extend for DOCX, TXT, CSV, JSON, and Markdown

---

## Unit Test Coverage

| Test Case | Status |
|-----------|--------|
| Initialization | ✅ Passed |
| Directory Not Found | ✅ Passed |
| Path is Not Directory | ✅ Passed |
| No Supported Documents | ✅ Passed |
| Successful PDF Loading | ✅ Passed |
| PDF Loading Failure | ✅ Passed |

---

## Phase Status

**Phase 5 Completed Successfully**

- Enterprise Document Loader implemented
- Enterprise logging integrated
- Enterprise exception handling integrated
- 6/6 Unit Tests Passed
- Ready for Phase 6 – Enterprise Text Splitter Framework

**phase 6 complted successsfully

Update:

Project Overview
Features
Project Structure
Phase 6 Completed
Enterprise Text Splitter Framework
Testing Status