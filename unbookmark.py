from dotenv import load_dotenv
import os
from mastodon import Mastodon
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
instance_url = os.getenv('MASTODON_INSTANCE_URL')
access_token = os.getenv('MASTODON_ACCESS_TOKEN')

# Load bookmarks from bookmarks.json
with open('bookmarks.json', 'r') as json_file:
    bookmarks_data = json.load(json_file)

# Initialize Mastodon client
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance_url
)

# Iterate through each bookmarked item and unbookmark it
for item in bookmarks_data:
    status_id = item['status_id']
    
    try:
        mastodon.status_unbookmark(status_id)
        print(f"Unbookmarked status {status_id}")
    except Exception as e:
        print(f"Failed to unbookmark status {status_id}: {e}")

print("Unbookmarking process complete.")
