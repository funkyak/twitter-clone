import sqlite3
import random
import json
import requests

# SQLite Database interaction to get user credentials
def get_user_credentials():
    # Connect to SQLite database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Query to select a random user from the users table
    c.execute("SELECT username, password FROM users ORDER BY RANDOM() LIMIT 1")
    user_data = c.fetchone()

    # Close the connection
    conn.close()
    
    return user_data

# Example list of tweets under 100 characters
EXAMPLE_TWEETS = [
    "Just finished my first cup of coffee for the day! Let's get this day started.",  # 74 characters
    "Loving the sunny weather today. It's a perfect day for a walk in the park.",  # 74 characters
    "Did anyone else see that new movie last night? Absolutely amazing! #MovieNight",  # 84 characters
    "Excited to see what this new week has in store. Time to grind! 💪",  # 74 characters
    "Random thought: Why do cats always look like they're judging you? 😸",  # 74 characters
    "Is it just me, or is the weekend always over way too fast?",  # 68 characters
    "Coffee in hand, ready to take on the world! #MondayMotivation",  # 74 characters
    "Can we all just agree that pizza is the best food ever? 🍕",  # 62 characters
    "Tried a new recipe today – turned out delicious! 🍳 #HomeCooked",  # 72 characters
    "Sometimes, the best days are the ones spent doing absolutely nothing."  # 74 characters
]

# Function to randomly select a tweet from the list
def generate_random_tweet():
    return random.choice(EXAMPLE_TWEETS)

# Function to login and return cookies (simulating login)
def login(username, password):
    url = "http://localhost:5000/api/login"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"username": username, "password": password})

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        # Save the cookie to be used for subsequent requests
        cookies = response.cookies
        print("Login successful.")
        return cookies
    else:
        print("Login failed:", response.status_code)
        return None

# Function to post a tweet using the provided cookie
def create_tweet(tweet, cookies):
    url = "http://localhost:5000/api/create_tweet"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"tweet": tweet})

    response = requests.post(url, headers=headers, data=data, cookies=cookies)

    if response.status_code == 200:
        print("Tweet posted successfully.")
    else:
        print(f"Failed to post tweet: {response.status_code}, {response.text}")

def main():
    # Step 1: Get random user credentials from the database
    user_data = get_user_credentials()
    if user_data is None:
        print("No users found in the database.")
        return
    
    username, password = user_data
    print(f"Using credentials: Username: {username}, Password: {password}")
    
    # Step 2: Login to the API and get the cookies for posting tweets
    cookies = login(username, password)
    if cookies is None:
        print("Login failed, cannot post tweet.")
        return

    # Step 3: Generate a random tweet from the list
    random_tweet = generate_random_tweet()
    print(f"Generated tweet: {random_tweet}")
    
    # Step 4: Post the generated tweet
    create_tweet(random_tweet, cookies)

if __name__ == "__main__":
    main()
