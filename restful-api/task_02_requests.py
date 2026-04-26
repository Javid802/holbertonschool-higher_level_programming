import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    try:
        response = requests.get(URL)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()

            for post in posts:
                print(post.get("title"))
        else:
            print("Failed to fetch posts.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def fetch_and_save_posts():
    try:
        response = requests.get(URL)

        if response.status_code == 200:
            posts = response.json()

            # Create structured list of dictionaries
            structured_posts = [
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body"),
                }
                for post in posts
            ]

            # Write to CSV
            with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(structured_posts)

        else:
            print("Failed to fetch posts.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
