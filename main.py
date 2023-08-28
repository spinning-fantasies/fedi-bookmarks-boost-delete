import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
instance_url = os.getenv('MASTODON_INSTANCE_URL')
access_token = os.getenv('MASTODON_ACCESS_TOKEN')

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Load bookmarks.json
with open('bookmarks.json', 'r') as file:
    bookmarks_data = json.load(file)

# Calculate the date 15 days ago
fifteen_days_ago = datetime.now() - timedelta(days=15)

# Loop through statuses in bookmarks_data and boost if they are 15 days old
for status in bookmarks_data:
    status_date = datetime.strptime(status['created_at'], '%Y-%m-%d')
    if status_date <= fifteen_days_ago:
        status_id = status['status_id']
        boost_url = f'{instance_url}/api/v1/statuses/{status_id}/reblog'
        response = requests.post(boost_url, headers=headers)

        if response.status_code == 200:
            print(f"Boosted status with ID {status_id}")
        else:
            print(f"Error boosting status with ID {status_id}: {response.text}")
