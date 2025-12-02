import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAALk15gEAAAAAD16pzdVNBKE5AseXbYR%2BR4UXMjc%3DarGCp40hz8zwnX8vXiuecmrcdQb4zvGBnbF3yIbAOuedhxCtc7"

client = tweepy.Client(
    bearer_token=bearer_token,
    wait_on_rate_limit=True
)

# -----------------------------
# BETTER KEYWORDS
# -----------------------------
tweet_query = '(cybersecurity OR infosec OR "security analyst" OR pentest OR bug bounty OR art OR design OR photoshop) -is:retweet lang:en'

gender_keywords = ["she", "her", "girl", "woman", "women in tech"]
india_keywords = [
    "india", "delhi", "mumbai", "bangalore", "bengaluru", "hyderabad", "pune",
    "kolkata", "chennai", "gujarat", "kerala", "tamil nadu", "uttar pradesh"
]
cyber_keywords = ["security", "cyber", "infosec", "pentest", "bug bounty", "red team", "blue team","tech"]

# -----------------------------
# FETCH TWEETS
# -----------------------------
def search_tweets():
    results = client.search_recent_tweets(
        query=tweet_query,
        max_results=100,
        tweet_fields=["author_id", "created_at"]
    )

    tweet_data = []
    if results.data:
        for tweet in results.data:
            tweet_data.append(tweet.author_id)

    return list(set(tweet_data))


# -----------------------------
# CHECK USERS
# -----------------------------
def find_matching_users():
    user_ids = search_tweets()
    matches = []

    # Batch into chunks of 100 (API limit)
    chunk_size = 100
    chunks = [user_ids[i:i+chunk_size] for i in range(0, len(user_ids), chunk_size)]

    for chunk in chunks:
        try:
            users = client.get_users(
                ids=chunk,
                user_fields=["description", "location", "name"]
            )

            if not users.data:
                continue

            for user in users.data:
                bio = (user.description or "").lower()
                loc = (user.location or "").lower()

                score = 0
                if any(k in bio for k in gender_keywords): score += 1
                if any(k in bio or k in loc for k in india_keywords): score += 1
                if any(k in bio for k in cyber_keywords): score += 1

                if score >= 2:
                    matches.append({
                        "username": user.username,
                        "name": user.name,
                        "bio": user.description,
                        "location": user.location
                    })

        except Exception as e:
            print("Error:", e)
            continue

    return matches



# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    results = find_matching_users()

    print("\n=== MATCHED USERS ===\n")
    for u in results:
        print(f"@{u['username']} - {u['name']}")
        print(f"Bio: {u['bio']}")
        print(f"Location: {u['location']}")
        print("-" * 40)
