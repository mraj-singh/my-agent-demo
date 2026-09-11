# Contributing Guide

## Table of Contents
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Submitting Pull Requests](#submitting-pull-requests)

## How to Contribute
We welcome contributions! Follow these steps to get started:
1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<your-username>/github-agent-demo.git
   cd github-agent-demo
   ```
3. **Create a new branch** for your work:
   ```bash
   git checkout -b <branch-name>
   ```
4. Make your changes, ensuring they adhere to the coding standards below.
5. Run the test suite to verify everything passes:
   ```bash
   python -m unittest discover -s tests -v
   ```
6. Commit your changes following the commit message guidelines.
7. Push the branch to your fork and open a Pull Request.

## Coding Standards
- **Python version**: 3.8+
- Follow **PEP 8** style guidelines. Use `flake8` or similar linting tools.
- Keep line length to **79 characters** where possible.
- Use **snake_case** for variables and functions, **PascalCase** for classes.
- Add **type hints** to public functions.
- Write **docstrings** for all modules, classes, and public functions using the Google style.
- Ensure new code is **covered by tests**.

## Commit Message Guidelines
We use a simple conventional commit style:
```
<type>(<scope>): <subject>

<body>

<footer>
```
- **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **scope** (optional): the area of the codebase, e.g., `app`, `tests`
- **subject**: short description, max 50 characters, capitalized, no period.
- **body** (optional): detailed explanation, wrapped at 72 characters.
- **footer** (optional): references to issues, e.g., `Closes #12`.

Example:
```
feat(app): add support for deleting tasks

Implemented a new endpoint to delete tasks by ID. Updated the task manager
logic and added corresponding unit tests.

Closes #5
```

## Submitting Pull Requests
1. **Sync your fork** with the upstream `main` branch before creating a PR.
2. Ensure **all checks pass** (tests, linting).
3. Provide a clear **description** of what the PR does and why.
4. Reference any related issues using `Closes #<issue-number>`.
5. Request a review from the maintainers.

We aim to review PRs within **48 hours**. Thank you for your contribution!
