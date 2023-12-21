#!/usr/bin/python3
"""a module to get data from an API"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(base_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Filter completed and total tasks
    completed_tasks = [task['title'] for task in todos_data if task['completed']]
    total_tasks = len(todos_data)
    number_of_completed_tasks = len(completed_tasks)

    # Display progress
    print(f"Employee {user_data['name']} is done with tasks({number_of_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
