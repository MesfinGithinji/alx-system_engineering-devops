#!/usr/bin/python3
"""Retrieves some data from an API"""

import requests
import sys


if __name__ == "__main__":
    
    api_url = "https://jsonplaceholder.typicode.com/"

    user_info = requests.get(api_url + "users/{}".format(sys.argv[1])).json()

    todos = requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user_info.get("name"), len(completed), len(todos)))

    [print("\t {}".format(c)) for c in completed]
