#!/usr/bin/env python3
"""
Module to fetch and process API data using the requests module.
Includes functions to fetch API data, display it, and save it as a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder API and prints the first 5 post titles.

    Prints:
        - HTTP status code of the response.
        - Titles of the first 5 posts if the request is successful.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            posts = response.json
            print("\nFirst 5 Post Titles:")
            for post in posts[:5]:
                print(f"- {post['title']}")
        else:
            print("Error: Unable to fetch posts.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder API and saves them as a CSV file.

    Creates:
        - A CSV file `posts.csv` containing post IDs, titles, and bodies.

    Prints:
        - Success message if data is saved successfully.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            # Define CSV file and column headers
            filename = "posts.csv"
            fieldnames = ["id", "title", "body"]

            # Write data to CSV file
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Write CSV headers
                writer.writerows(posts)  # Write API data to file

            print(f"Data successfully saved to {filename}")

        else:
            print("Error: Unable to fetch posts.")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
