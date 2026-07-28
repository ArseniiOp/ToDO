class Task:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def decomplete(self):
        self.completed = False





