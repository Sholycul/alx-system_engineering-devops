#/usr/bin/python3

"""
This module uses the jsonplaceholder fake api to get users todo
 API to display number of tasks done and the progress in general
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:

        id_ = int(sys.argv[1])

        user_url = f"https://jsonplaceholder.typicode.com/users/{id_}"
        todo_url = f"{user_url}/todos"

        users = requests.get(user_url)
        user_data = users.json()

        EMPLOYEE_NAME = user_data["name"]

        todos = requests.get(todo_url)
        todo_data = todos.json()

        NUMBER_OF_DONE_TASKS = sum(task.get("completed", False) for task in todo_data)
        TOTAL_NUMBER_OF_TASKS = len(todo_data)
        
        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in todo_data:
            if task.get('completed', True):
                print("\t {}".format(task.get("title")))
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
