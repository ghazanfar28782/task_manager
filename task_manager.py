# task_manager.py

from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, title: str):
        self.tasks = [task for task in self.tasks if task.title != title]

    def list_tasks(self):
        return sorted(self.tasks, key=lambda x: (x.deadline, x.priority))
