Interview Questions

Now imagine you're in a Senior DevOps interview.

Q1

Why did you create a base exception instead of directly using Python's Exception?

Expected answer:

"I created a project-specific base exception to centralize the application's exception hierarchy. All custom exceptions inherit from it, which improves maintainability, consistency, and makes future enhancements easier while following the DRY principle."

Q2

Why didn't you put logging inside the exception class?

Expected answer:

"Because the exception framework should only represent errors. Logging is handled by the centralized logging framework. This follows the Single Responsibility Principle."

Q3

Why write unit tests for exceptions?

Expected answer:

"Unit tests verify that the exception hierarchy, inheritance, and behavior remain correct. If someone accidentally changes the inheritance or constructor in the future, the tests fail immediately, preventing regressions."