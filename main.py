# main.py

from task import Task
from task_manager import TaskManager
from datetime import datetime

# Example tasks creation
task1 = Task(
    title="Finish Python project",
    description="Complete the task management application",
    deadline=datetime(2024, 9, 10),
    priority=1
)

task2 = Task(
    title="Prepare for meeting",
    description="Get the slides ready for Monday's presentation",
    deadline=datetime(2024, 9, 8),
    priority=2
)

task3 = Task(
    title="Buy groceries",
    description="Get milk, eggs, and bread from the store",
    deadline=datetime(2024, 9, 7),
    priority=3
)

# Initialize TaskManager and add tasks
task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

# List all tasks
print("Tasks before removal:")
for task in task_manager.list_tasks():
    print(f"Title: {task.title}, Deadline: {task.deadline}, Priority: {task.priority}")

# Remove a task
task_manager.remove_task("Prepare for meeting")

# List all tasks after removal
print("\nTasks after removal:")
for task in task_manager.list_tasks():
    print(f"Title: {task.title}, Deadline: {task.deadline}, Priority: {task.priority}")
