import requests
import random
import string
import time
import sqlite3

# --- SQLite Setup ---
def setup_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user_to_db(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Username {username} already exists in the database.")
    finally:
        conn.close()

# Initialize the database
setup_database()

# --- Name list ---
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

# --- User creation and login loop ---
base_url = "http://localhost:5000/api"
password = "SecurePassword123"

for i in range(1, 11):
    first_name = random.choice(names)
    random_letter = random.choice(string.ascii_uppercase)
    username = f"{first_name}{random_letter}"

    print(f"Generated Username: {username}")

    # API call to create user
    user_data = {
        "username": username,
        "email": f"{username}@example.com",
        "password": password
    }
    try:
        response = requests.post(f"{base_url}/create_user", json=user_data)
        print(f"User creation status: {response.status_code}")

        if response.status_code == 201:
            # Save to local SQLite DB
            add_user_to_db(username, password)

            # Login to get session
            session = requests.Session()
            login_response = session.post(f"{base_url}/login", json={"username": username, "password": password})
            print(f"Login status: {login_response.status_code}")

            # Optional tweet
            # tweet_response = session.post(f"{base_url}/create_tweet", json={"tweet": f"{username}'s first tweet!"})
            # print(f"Tweet status: {tweet_response.status_code}")
        else:
            print("Skipping DB entry due to API error.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    time.sleep(2)
