# Project Title

## Overview

This repository contains a minimalistic **Task Manager** written in Python. It serves as a learning sandbox for demonstrating GitHub automation, including creating branches, updating files, and opening pull requests. The core functionality includes adding tasks, listing them, and marking tasks as completed.

## Features

- **Add Task** – Create a new task with a title.
- **List Tasks** – Retrieve all current tasks.
- **Complete Task** – Mark a task as completed using its index.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   This project has no external dependencies beyond the Python standard library.
   ```bash
   pip install -r requirements.txt  # (file may be empty for now)
   ```

## Usage

Run the application directly to see a demo of adding and completing tasks:

```bash
python app.py
```

### Example in Python

```python
from app import add_task, list_tasks, complete_task

# Add tasks
add_task("Learn GitHub Agent")
add_task("Create my first pull request")

# List tasks
for i, task in enumerate(list_tasks(), start=1):
    status = "✓" if task["completed"] else " "
    print(f"[{status}] {i}. {task['title']}")

# Complete the first task
complete_task(0)
```

## Testing

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository** and create a new branch for your feature or bug fix.
2. **Write clear, concise commit messages**.
3. **Ensure all tests pass** and add new tests for added functionality.
4. **Update documentation** (README, docstrings) as needed.
5. **Submit a pull request** describing your changes.

For detailed contribution instructions, see the `CONTRIBUTING.md` file (if present).

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

*Happy coding!*
