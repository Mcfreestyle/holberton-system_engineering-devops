#!/usr/bin/python3
"""This module provides the `getTodo` and `exportCSV` functions"""
import csv
import requests
from sys import argv


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


def exportCSV(id_user, username, todo):
    """
    Exports data in CSV format
    Args:
        id_user = user id
        name = user name
        todo = all tasks of user
    """
    file_csv = str(id_user) + ".csv"
    data = [["2", username, task.get('completed'), task.get('title')]
            for task in todo]

    with open(file_csv, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    try:
        id_user = int(argv[1])
    except Exception:
        exit()

    (username, todo) = getTodo(id_user)
    exportCSV(id_user, username, todo)
