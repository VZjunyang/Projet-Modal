from TikTokApi import TikTokApi

api = TikTokApi()

def get_followers(username: str):
    # Get the user information
    user = api.getUser(username)
    
    # Get the user's follower count
    follower_count = user['userInfo']['stats']['followerCount']

    # Initialize variables
    followers = []
    cursor = 0
    batch_size = 30  # Number of users to fetch in one request (max is 30)

    # Fetch the followers in batches
    while len(followers) < follower_count:
        # Get a batch of followers
        batch = api.get_user_followers(user['userInfo']['user']['id'], cursor=cursor, count=batch_size)

        # Add the batch of followers to the list
        followers.extend(batch)

        # Move the cursor to the next batch
        cursor += batch_size

    return followers

username = "carlaginola"  # Replace with the target user's TikTok username
followers = get_followers(username)

print(f"Total followers: {len(followers)}")
for follower in followers:
    print(follower['uniqueId'])