#!/usr/bin/python3
"""This module provides the `getTodo` function"""
import requests
from sys import argv


def getTodo(id_user):
    """Returns information of id_user
    """
    url_api = "https://jsonplaceholder.typicode.com"

    url_user = "{}/users/{}".format(url_api, id_user)
    user = requests.get(url_user).json()
    name = user.get('name')

    url_todo = "{}/todos?userId={}".format(url_api, id_user)
    todo = requests.get(url_todo).json()
    nb_tasks = len(todo)

    tasks_compl = []
    for task in todo:
        if task.get('completed') is True:
            tasks_compl.append(task.get('title'))

    nb_compl = len(tasks_compl)

    info = "Employee {} is done with tasks({}/{}):"
    print(info.format(name, nb_compl, nb_tasks))
    for t in tasks_compl:
        print("\t {}".format(t))


if __name__ == '__main__':
    try:
        id_user = int(argv[1])
    except Exception:
        exit()

    getTodo(id_user)
