#!/usr/bin/python3
"""Exports data in the JSON format"""

from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(api_url)
    username = response.json().get('username')

    api_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    response = get(api_url)
    todos = response.json()
    dictionary = {user_id: []}
    for todo in todos:
        dictionary[user_id].append({
            "todo": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dictionary, file)
