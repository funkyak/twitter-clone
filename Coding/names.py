import requests
import random
import string
import time

# Combined list of male and female first names
names = [
    "Noah", "Theo", "Luca", "Arthur", "Oliver", "Archie", "George", "Leo", "Freddie", "Arlo",
    "Alfie", "Oscar", "Teddy", "Henry", "Albie", "Finley", "Jude", "Charlie", "Elijah", "Tommy",
    "Harry", "Oakley", "Hudson", "Roman", "Rory", "Reuben", "Louie", "Jack", "Reggie", "Lucas",
    "Theodore", "Ezra", "Isaac", "Thomas", "Jacob", "Max", "James", "Ethan", "Ronnie", "Frankie",
    "Rowan", "Harrison", "Adam", "Riley", "William", "Jaxon", "Grayson", "Caleb", "Mason", "Hunter",
    "Logan", "Hugo", "Sonny", "Jesse", "Vinnie", "Alexander", "Joshua", "Enzo", "Yusef", "Finn",
    "Austin", "Louis", "Cody", "Ollie", "Kai", "Musa", "Carter", "Yahya", "Edward", "Muhammed",
    "Bobby", "Stanley", "Joseph", "Milo", "Elliot", "Myles", "Dylan", "Eli", "Blake", "Alex",
    "Elias", "Jasper", "Zachary", "Elliot", "Chester", "Ralph", "Gabriel", "Brody", "Rupert",
    "Toby", "Albert", "Otis", "Ellis", "Daniel", "Liam", "Jenson", "Ruben", "David", "Jayden",
    "Jackson", "Amelia", "Olivia", "Isla", "Ava", "Sophia", "Mia", "Harper", "Evelyn", "Ella",
    "Abigail", "Scarlett", "Grace", "Chloe", "Lily", "Avery", "Sophie", "Hannah", "Aria",
    "Layla", "Zoe", "Nora", "Charlotte", "Camila", "Penelope", "Riley", "Leah", "Hazel", "Lucy",
    "Victoria", "Mila", "Ruby", "Luna", "Lila", "Ellie", "Nova", "Sadie", "Hannah", "Kinsley",
    "Addison", "Stella", "Bella", "Brooklyn", "Skylar", "Mackenzie", "Naomi", "Autumn", "Savannah",
    "Sadie", "Everly"
]

# API base URL
base_url = "http://localhost:5000/api"

# Create and login users
for i in range(1, 101):
    first_name = random.choice(names)
    random_letter = random.choice(string.ascii_uppercase)
    username = f"{first_name}{random_letter}"

    print(f"Generated Username: {username}")

    # Create user
    user_data = {
        "username": username,
        "email": f"{username}@example.com",
        "password": "SecurePassword123"
    }
    create_user_response = requests.post(f"{base_url}/create_user", json=user_data)
    print(f"User creation status: {create_user_response.status_code}")

    # Login user
    session = requests.Session()
    login_data = {
        "username": username,
        "password": "SecurePassword123"
    }
    login_response = session.post(f"{base_url}/login", json=login_data)
    print(f"Login status: {login_response.status_code}")

    # Optionally post a tweet
    # tweet_data = {"tweet": f"{username}'s first tweet!"}
    # tweet_response = session.post(f"{base_url}/create_tweet", json=tweet_data)
    # print(f"Tweet status: {tweet_response.status_code}")

    time.sleep(2)
