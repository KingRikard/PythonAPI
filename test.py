import requests

URL = "https://jsonplaceholder.typicode.com/users"

print("Search by Username:")
user = input("> ")
queryURL = URL + f"?username={user}"

response = requests.get(queryURL)

print(response.text)

