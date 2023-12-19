#!/usr/bin/python3
"""script that use rest api for a given employee ID"""
import requests
import sys
import csv


def export_to_csv(employee_id):
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

        # Prepare CSV filename
        csv_filename = f"{employee_id}.csv"

        # Write data to CSV file
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            # Write each task to CSV
            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

        print(f"Data exported to {csv_filename} successfully!")

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
