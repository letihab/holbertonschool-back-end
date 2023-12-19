#!/usr/bin/python3
"""script that use rest api for a given employee ID"""
import requests
import json

def export_all_to_json():
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    try:
        # Fetch all users
        users_response = requests.get(users_url)
        users_data = users_response.json()

        # Fetch all todos
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create a dictionary to store data
        all_data = {}
        for user in users_data:
            user_id = user['id']
            username = user['username']
            user_todos = []

            # Collect todos for each user
            for todo in todos_data:
                if todo['userId'] == user_id:
                    user_todos.append({
                        'username': username,
                        'task': todo['title'],
                        'completed': todo['completed']
                    })

            # Store user todos in the dictionary
            all_data[user_id] = user_todos

        # Write data to JSON file
        json_filename = 'todo_all_employees.json'
        with open(json_filename, 'w') as json_file:
            json.dump(all_data, json_file, indent=4)

        print(f"Data exported to {json_filename} successfully!")

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    export_all_to_json()
