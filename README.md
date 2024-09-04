# Task Management Application

This is a Task Management application written in Python. The application allows users to create tasks, list them by deadline and priority, and remove tasks when completed.

## Project Structure

The project is organized into the following files:

### 1. `task.py`
Defines the `Task` class, which represents an individual task with the following attributes:
- `title`: The title of the task.
- `description`: A brief description of the task.
- `deadline`: The deadline for the task (as a `datetime` object).
- `priority`: The priority level of the task.

### 2. `task_manager.py`
Contains the `TaskManager` class, which manages a list of tasks. It provides the following methods:
- `add_task(task)`: Adds a new task to the list.
- `remove_task(title)`: Removes a task from the list based on its title.
- `list_tasks()`: Returns the tasks sorted by their deadline and priority.

### 3. `main.py`
This script is used to create sample tasks, add them to the `TaskManager`, and test the functionality of listing and removing tasks.

## Getting Started

### Prerequisites

- Python 3.6 or higher
