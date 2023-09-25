#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

from json import dump
from requests import get


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(api_url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)
        api_url = api_url + '/todos/'
        response = get(api_url)
        todos = response.json()
        dictionary[user_id] = []
        for todo in todos:
            dictionary[user_id].append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)
