#!/usr/bin/python3
"""script that use rest api for a given employee ID"""
import requests
import sys
import json


def export_to_json(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare data in JSON format
        json_data = {str(employee_id): []}
        for task in todos_data:
            json_data[str(employee_id)].append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_name
            })

        # Write data to JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_filename} successfully!")

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
