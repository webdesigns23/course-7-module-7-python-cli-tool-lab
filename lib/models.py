# lib/models.py

# TODO: Define the Task class
# Each task should store a title and a completion status (initially False)
class Task:
    def __init__(self, title):
        # TODO: Set the title and initialize completed to False
        pass

    def complete(self):
        # TODO: Mark task as complete and print confirmation
        pass

# TODO: Define the User class
# Each user should have a name and a list of tasks
class User:
    def __init__(self, name):
        # TODO: Set the name and initialize the task list
        pass

    def add_task(self, task):
        # TODO: Append the task to the user's list and print confirmation
        pass

    def get_task_by_title(self, title):
        # TODO: Return the task if the title matches, or return None
        pass
