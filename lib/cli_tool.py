# lib/cli_tool.py

import argparse
from lib.models import Task, User

# Global in-memory dictionary to hold user-task mappings
users = {}

# TODO: Define a function to add a task
def add_task(args):
    # TODO:
    # - Get or create a User instance
    # - Create a Task from the input title
    # - Add the Task to the User
    pass

# TODO: Define a function to complete a task
def complete_task(args):
    # TODO:
    # - Find the user by name
    # - Use get_task_by_title to find the task
    # - Call the complete method or print an error
    pass

# Main CLI handler using argparse
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding a task
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing a task
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

# Entry point
if __name__ == "__main__":
    main()
