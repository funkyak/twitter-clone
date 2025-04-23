import sqlite3

# Connect to the SQLite database
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
        else:
            print("No tweets found")

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage - Fetch the most recent tweet
get_most_recent_tweet()
