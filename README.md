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


###########################################################
PHASE 7
# 🚀 Enterprise AI DevOps Copilot

An enterprise-grade AI-powered DevOps assistant built using **Python**, **LangChain**, **Ollama**, **ChromaDB**, and **RAG Architecture**.

The project follows enterprise software engineering principles, including modular architecture, structured logging, custom exception handling, comprehensive unit testing, and detailed documentation.

---

# 📌 Project Progress

| Phase | Status |
|--------|--------|
| ✅ Phase 1 - Enterprise Project Structure | Completed |
| ✅ Phase 2 - Enterprise Logging Framework | Completed |
| ✅ Phase 3 - Enterprise Exception Framework | Completed |
| ✅ Phase 4 - Enterprise File Utility Framework | Completed |
| ✅ Phase 5 - Enterprise Document Loader | Completed |
| ✅ Phase 6 - Enterprise Text Splitter | Completed |
| ✅ Phase 7 - Enterprise Embedding Engine | Completed |
| ⏳ Phase 8 - Enterprise Vector Store (ChromaDB) | Next |

---

# ✅ Phase 7 - Enterprise Embedding Engine

## Overview

The Enterprise Embedding Engine converts processed documents into dense vector embeddings using LangChain and Ollama.

The generated embeddings will be stored in ChromaDB during the next phase to enable semantic search and Retrieval-Augmented Generation (RAG).

---

## Features

- Enterprise Embedding Engine
- Ollama Embedding Integration
- LangChain Document Support
- Input Validation
- Enterprise Logging
- Custom Exception Handling
- Enterprise Architecture
- Comprehensive Unit Testing

---

## Technologies Used

- Python 3.12
- LangChain
- LangChain-Ollama
- Ollama
- Pytest
- Logging Framework
- Custom Exception Framework

---

# Embedding Workflow

```
PDF Documents
       │
       ▼
Document Loader
       │
       ▼
Text Splitter
       │
       ▼
Document Chunks
       │
       ▼
Embedding Engine
       │
       ▼
Dense Vector Embeddings
       │
       ▼
ChromaDB (Phase 8)
```

---

# Enterprise Design Principles

This module follows enterprise software engineering best practices.

- Single Responsibility Principle (SRP)
- Modular Architecture
- Custom Exception Handling
- Structured Logging
- Configuration Management
- Unit Testing
- Input Validation
- Clean Code Practices

---

# Unit Testing

The Embedding Engine includes enterprise-grade unit tests covering:

- Engine Initialization
- None Input Validation
- Empty List Validation
- Invalid Input Type
- Successful Embedding Generation
- Embedding Failure Handling

Current Test Status

```
6 Tests Passed
```

---

# Folder Structure

```
enterprise-ai-devops-copilot/
│
├── app/
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│
├── config/
│
├── utils/
│   ├── logger.py
│   ├── exceptions.py
│   ├── file_utils.py
│
├── tests/
│   ├── test_embedding.py
│
├── docs/
│   ├── debugging/
│   ├── interview_notes/
│
├── logs/
│
└── README.md
```

---

# Project Highlights

✔ Enterprise Project Structure

✔ Structured Logging Framework

✔ Custom Exception Framework

✔ Enterprise File Utilities

✔ Enterprise PDF Loader

✔ Enterprise Text Splitter

✔ Enterprise Embedding Engine

✔ Unit Tested Components

✔ Production Ready Architecture

---

# Next Phase

## Phase 8 – Enterprise Vector Store (ChromaDB)

Upcoming features include:

- ChromaDB Integration
- Persistent Vector Storage
- Metadata Storage
- Similarity Search
- Semantic Retrieval
- Enterprise Exception Handling
- Unit Testing
- RAG Integration

---

# Author

**Vishesh Pachauri**

Senior DevOps Engineer

Enterprise AI | DevOps | Python | AWS | Kubernetes | Terraform | LangChain | Ollama | RAG