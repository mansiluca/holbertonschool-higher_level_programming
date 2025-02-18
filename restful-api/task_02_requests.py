#!/usr/bin/python3
"""
This module fetches posts from a RESTful API and prints them to the console
or saves them to a file.
"""


import csv
import requests


def fetch_and_print_posts():
    """
    fetches and prints all posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    fetches and saves all posts to a file
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow(
                    {"id": post["id"], "title": post["title"],
                     "body": post["body"]})
