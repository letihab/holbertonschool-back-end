#!/usr/bin/python3
""" get data from an API"""
from sys import argv
import json
import requests


def get_employee_todos(user_id):
    """get the reponse and format and print data"""
    number_completed = 0

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    employee_name = user.get("username")

    data = {
        user_id:
            [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee_name
                } for task in todos
            ]
            }

    file_name = user_id + ".json"

    with open(file_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    """main function"""
    get_employee_todos(argv[1])
