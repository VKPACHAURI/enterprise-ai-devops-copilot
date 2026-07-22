If an interviewer asks:

Why do we pass __name__ to get_logger()?

You can answer:

We pass __name__ so that each module automatically creates a logger with its own module name. This makes log messages traceable because every entry identifies which part of the application generated it. During debugging and production support, this helps engineers quickly locate the source of an issue without manually assigning logger names in every file.


---
What is __name__?

__name__ is a special built-in Python variable.

Every Python file automatically gets a __name__ value.
---
Interview Question

Why did you create a get_logger() function instead of configuring logging in every module?

A strong answer is:

I created a reusable factory function that returns a fully configured logger. This centralizes the logging configuration, eliminates duplicate setup code, enforces consistency across the application, and makes future changes easy because the configuration is maintained in a single location

Interview Answer

If an interviewer asks:

Why do you call logger.setLevel()?

You can answer:

logger.setLevel() defines the minimum severity level that the logger will process. Messages below that level are ignored. This allows us to control the amount of logging generated in different environments, such as using DEBUG during development and INFO or WARNING in production

---
Interview Answer

If an interviewer asks:

What did you implement in Phase 2?

You can answer:

"I designed and implemented a centralized enterprise logging framework for the application. Instead of using print() statements, I created a reusable logger utility that supports both console and file logging. I added structured formatting with timestamps, log levels, and module names, prevented duplicate handlers, automatically created the log directory, and centralized the configuration. This makes debugging, monitoring, and root cause analysis much easier in production environments."

That's a strong, professional answer.

..
