"""A tiny task manager for GitHub Agent practice."""

tasks = []


def add_task(title):
    """Add a new task and return it."""
    task = {"title": title, "completed": False}
    tasks.append(task)
    return task


def list_tasks():
    """Return all tasks."""
    return tasks


def complete_task(index):
    """Mark a task as completed by its zero-based index."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Task not found")

    tasks[index]["completed"] = True
    return tasks[index]


if __name__ == "__main__":
    add_task("Learn GitHub Agent")
    add_task("Create my first pull request")

    for i, task in enumerate(list_tasks(), start=1):
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {i}. {task['title']}")
