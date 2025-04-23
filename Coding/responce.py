import sqlite3
import random
import json
import requests

# SQLite Database interaction to get user credentials
def get_user_credentials():
    # Connect to SQLite database
    conn = sqlite3.connect('users.db')  # Ensure this path is correct
    c = conn.cursor()

    # Query to select a random user from the users table
    c.execute("SELECT username, password FROM users ORDER BY RANDOM() LIMIT 1")
    user_data = c.fetchone()

    # Close the connection
    conn.close()

    return user_data

# Example list of responses to tweets
EXAMPLE_RESPONSES = [
    "Totally feel the same way!",
    "Haha, that's so true!",
    "Couldn't agree more 👏",
    "Interesting take! Here's mine...",
    "Love this! Thanks for sharing 🙌",
    "That's a vibe 😎",
    "Real talk right there.",
    "Absolutely! 🙌",
    "Big mood!",
    "Facts only 💯"
]

# Function to generate a random tweet from the list
def generate_random_tweet():
    return random.choice(EXAMPLE_RESPONSES)

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

# Connect to the SQLite database for the most recent tweet
def connect_to_db():
    try:
        conn = sqlite3.connect('/mnt/c/Users/R23M/Documents/twitter-clone/modules/database.db')  # Adjust path if needed
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to fetch the most recent tweet and link to username
def get_most_recent_tweet():
    try:
        # Connect to the database
        conn = connect_to_db()
        if conn is None:
            print("Failed to connect to the database.")
            return

        cursor = conn.cursor()

        # Query to select the most recent tweet by ordering by the highest ID (most recent post)
        cursor.execute("""
            SELECT p.id, p.tweet, p.stamp, p.post_img, p.user_id, u.username
            FROM post p
            JOIN user_mgmt u ON p.user_id = u.id
            ORDER BY p.id DESC
            LIMIT 1
        """)
        tweet = cursor.fetchone()

        # Check if the tweet exists
        if tweet:
            tweet_id, tweet_content, timestamp, post_img, user_id, username = tweet
            print(f"{tweet_id}, {tweet_content}, {username}")
            return tweet  # Return the tweet data
        else:
            print("No tweets found")
            return None

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Main function to control the flow
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

    # Step 3: Generate and post a random tweet
    random_tweet = generate_random_tweet()
    print(f"Generated tweet: {random_tweet}")
    create_tweet(random_tweet, cookies)

    # Step 4: Optionally, get the most recent tweet (if needed for additional logic)
    print("🔍 Fetching the most recent tweet from the database...")
    recent_tweet = get_most_recent_tweet()
    if recent_tweet:
        print(f"📢 Most recent tweet: {recent_tweet[1]} by @{recent_tweet[5]}")
    else:
        print("⚠️ No recent tweet found.")

if __name__ == "__main__":
    main()
