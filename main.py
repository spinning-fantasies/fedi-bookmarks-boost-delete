from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
instance_url = os.getenv('MASTODON_INSTANCE_URL')
access_token = os.getenv('MASTODON_ACCESS_TOKEN')

# Endpoint for getting bookmarks
bookmarks_endpoint = f'{instance_url}/api/v1/bookmarks'
print(bookmarks_endpoint)

# Set the authorization header
headers = {
    'Authorization': f'Bearer {access_token}'
}
print(headers)
