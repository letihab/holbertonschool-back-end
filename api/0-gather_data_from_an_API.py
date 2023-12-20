#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
import requests
import sys

def gather_data_from_api(user_id):
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{user_id}/todos"
    name_url = f"{main_url}/users/{user_id}"
    
    todo_response = requests.get(todo_url)
    name_response = requests.get(name_url)
    
    if todo_response.status_code != 200 or name_response.status_code != 200:
        print("Failed to fetch data. Please check the user ID.")
        return
    
    todo_result = todo_response.json()
    name_result = name_response.json()
    
    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result if todo.get("completed")])
    name = name_result.get("name")
    
    print(f"Employee {name} is done with tasks ({todo_complete}/{todo_num}):")
    
    for todo in todo_result:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py user_id")
    else:
        user_id = sys.argv[1]
        gather_data_from_api(user_id)
