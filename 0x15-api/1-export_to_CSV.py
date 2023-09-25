#!/usr/bin/python3
"""Retrieves data and then exports to a CSV"""

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
    with open('{}.csv'.format(user_id), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, todo.get('completed'),
                               todo.get('title')))
