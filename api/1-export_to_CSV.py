#!/usr/bin/python3
"""a module to get data from an API"""
from sys import argv
import csv
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

    for task in todos:
        if task.get("completed"):
            number_completed += 1

    data = [
        ["userId", "userName", "completed", "title"]
    ]

    for task in todos:
        newrow = [task.get("userId"), employee_name,
                  task.get("completed"), task.get("title")]
        data.append(newrow)

        file_name = user_id + ".csv"

    with open(file_name, mode="w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data[1:])

        print(user)


if __name__ == "__main__":
    """main function"""
    get_employee_todos(argv[1])
