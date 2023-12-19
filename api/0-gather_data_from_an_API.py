#!/usr/bin/python3
"""Script that uses a REST API for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employe_name = employee_data['name']

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate progress
        totalt = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        num_ttask = len(completed_tasks)

        # Display progress
        print(
            f"Employee {employe_name} is done with tasks ({num_ttask}/{totalt}):"
        )
        print(f"{employe_name}: {num_ttask}/{totalt}")

        # Display completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print("Error fetching data:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
