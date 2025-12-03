import requests

username = "Timmohitibi"

# Function to get all followers or following
def get_users(url):
    users = []
    page = 1
    while True:
        r = requests.get(f"{url}?page={page}&per_page=100")
        data = r.json()
        if not data:
            break
        users.extend([user['login'] for user in data])
        page += 1
    return users

# Get followers
followers = get_users(f"https://api.github.com/users/{username}/followers")

# Get following
following = get_users(f"https://api.github.com/users/{username}/following")

# Find who is not following back
not_following_back = [user for user in following if user not in followers]

print(f"People {username} follows who are not following back:")
for user in not_following_back:
    print(user)

