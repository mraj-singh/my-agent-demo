# GitHub Agent Demo

A tiny Python project used as a safe sandbox for learning GitHub Agent / multi-agent GitHub automation.

## Project

This project is a simple task manager with three operations:
- Add a task
- List tasks
- Complete a task

The project is intentionally small so an AI agent can safely modify it, create branches, and raise pull requests.

## Run

```bash
python app.py
```

## Test

```bash
python -m unittest discover -s tests -v
```
