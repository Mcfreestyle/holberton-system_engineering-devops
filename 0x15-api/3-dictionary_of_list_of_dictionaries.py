#!/usr/bin/python3
"""
This module provides the `getNumbersUsers`, `getTodo`, `getJsonUser` functions
"""
import json
import requests


def getNumberUsers():
    """Returns the numbers of users"""
    url_users = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url_users).json()
    return (len(users))


def getTodo(id_user):
    """Returns information of id_user
    """
    url_api = "https://jsonplaceholder.typicode.com"

    url_user = "{}/users/{}".format(url_api, id_user)
    user = requests.get(url_user).json()
    username = user.get('username')

    url_todo = "{}/todos?userId={}".format(url_api, id_user)
    todo = requests.get(url_todo).json()

    info = (username, todo)
    return (info)


def getJsonUser(id_user, username, todo):
    """
    Return a user data in the JSON format
    Args:
        id_user = user id
        name = user name
        todo = all tasks of user
    """
    data = {id_user: [{
                       "username": username,
                       "task": task.get('title'),
                       "completed": task.get('completed')
                      } for task in todo]}

    return (data)


if __name__ == '__main__':

    nb_users = getNumberUsers()
    dict_all = {}
    for i in range(nb_users):
        (username, todo) = getTodo(i + 1)
        data = getJsonUser(i + 1, username, todo)
        dict_all.update(data)

    with open("todo_all_employees.json", "w") as f:
        json.dump(dict_all, f)
