import sqlite3




class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER NOT NULL)
        ''')

    def add_task(self, title, completed):
        self.cursor.execute('''
                            INSERT INTO tasks (title, completed)
                            VALUES (?, ?)''',
                            (title, completed))

    def delete_task(self, task_id):
        self.cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
        self.connection.commit()

    def get_tasks(self):
        self.cursor.execute('''SELECT * FROM tasks''')
        tasks = self.cursor.fetchall()
        result = []
        self.connection.commit()
        from task import Task
        for task in tasks:
            task_id, title, completed = task
            task_object = Task(task_id, title, completed)
            result.append(task_object)


        return result

    def update_task(self, completed, task_id):
        self.cursor.execute('''UPDATE tasks
            SET completed = ?
            WHERE id = ?''', (completed, task_id))
        self.connection.commit()

