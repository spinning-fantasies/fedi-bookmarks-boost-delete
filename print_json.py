from dotenv import load_dotenv
import os
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
instance_url = os.getenv('MASTODON_INSTANCE_URL')
access_token = os.getenv('MASTODON_ACCESS_TOKEN')

# Initialize variables
all_bookmarks = []
next_max_id = None

while True:
    # Construct the API endpoint URL
    endpoint = f'{instance_url}/api/v1/bookmarks'

    # Set up headers with the access token
    headers = {'Authorization': f'Bearer {access_token}'}

    # Set up parameters for pagination
    params = {'max_id': next_max_id} if next_max_id else {}

    # Make the API request
    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        bookmarks = response.json()

        # Append the current page of bookmarks to the list
        all_bookmarks.extend(bookmarks)

        # Check if there are more pages
        if 'Link' in response.headers:
            link_header = response.headers['Link']
            if 'rel="next"' in link_header:
                next_max_id = link_header.split('max_id=')[1].split('&')[0]
            else:
                break
        else:
            break
    else:
        print(f"Error fetching bookmarks. Status code: {response.status_code}")
        break

# Now all_bookmarks contains all the bookmarked statuses
print("Total bookmarked statuses:", len(all_bookmarks))

data = []

for x in range(0, len(all_bookmarks)):
    # print(all_bookmarks[x]['created_at'], all_bookmarks[x]['url'])

    data.append({
        "status_id": all_bookmarks[x]['id'],
        "created_at": all_bookmarks[x]['created_at'].format().split("T")[0],
        "url": all_bookmarks[x]['url']
    })

    # Specify the file name
    filename = "bookmarks.json"

    # Write the data to a JSON file
    with open(filename, "w") as json_file:
        json.dump(data, json_file)
        
print(f"JSON file {filename} created successfully.")