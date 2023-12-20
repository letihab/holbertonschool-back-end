#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
from sys import argv
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

    employee_name = user.get("name")

    for task in todos:
        if task.get("completed"):
            number_completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_completed, len(todos)))
    for task in todos:
        if task.get("completed"):
            formated_title = "	 " + task.get("title")
            print("{}".format(formated_title))


if __name__ == "__main__":
    """main function"""
    get_employee_todos(argv[1])
