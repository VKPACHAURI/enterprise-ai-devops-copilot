# constants.py

Why did you create constants.py?

Answer:

To centralize fixed application values and avoid hardcoding them throughout the project. This improves maintainability and follows the Single Responsibility Principle.

---

# settings.py

Why settings.py?

Stores runtime configuration and environment-specific values.

---
This Will Be Your Interview Handbook

By the end of the project, you'll have a document that answers questions like:

What problem does your project solve?
Why did you use WSL2 instead of developing directly on Windows?
Why did you separate settings.py and constants.py?
Why did you create a centralized logging system?
Why did you write unit tests first?
How does your AI assistant differ from a normal chatbot?
Why did you choose Ollama for local development?
How does your RAG pipeline work?
How does your multi-agent architecture coordinate tasks?
How would you deploy this project to production?

---
# Enterprise AI DevOps Copilot

## Why did you build this project?

Modern DevOps engineers spend significant time searching documentation, troubleshooting infrastructure issues, and performing repetitive operational tasks.

I wanted to build an AI-powered DevOps Copilot that can retrieve relevant knowledge, assist with troubleshooting, automate repetitive tasks, and improve engineer productivity.
---
6. How would I explain it in an interview?

A concise answer might be:

I started by building an enterprise-grade foundation instead of jumping directly into AI features. I separated runtime configuration from immutable constants, organized the project into clear modules, added unit tests, and documented the design. This makes the application easier to maintain, test, and extend as it grows. By investing in the architecture first, later features like logging, RAG, AI agents, and deployment can be added consistently without introducing unnecessary technical debt.

Interview Follow-up

If the interviewer asks:

What problem did you solve?

You can answer:

The main problem was the lack of a scalable and maintainable foundation. Many projects begin with hardcoded values, scattered configuration, and little testing. I solved this by creating a centralized configuration module, separating constants from runtime settings, organizing the project using the Single Responsibility Principle, and adding automated tests. This provides a stable foundation for building enterprise AI capabilities.

Why We're Following This Process

Every phase of this project will answer the same six questions:

Problem
      ↓
Reason
      ↓
Solution
      ↓
Design Decision
      ↓
Business Value
      ↓
Interview Explanation

This helps you think like an engineer who designs systems to solve business problems, not just someone who writes code.

