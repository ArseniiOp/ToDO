
from database import Database
class ToDo:
    tasks = []

    def __init__(self):
        self.database = Database()
        self.tasks = []

    def add_task(self, task):
        self.database.add_task(task.title, task.completed)


    def delete_task(self, task):
        self.database.delete_task(task.id)


    def get_tasks(self):
        return self.database.get_tasks()

    def get_task(self, title):
        for task in self.database.get_tasks():
            if task.title.lower() == title.lower():
                return task

    def update_task(self, task):
        self.database.update_task(task.completed, task.id)
