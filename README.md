# masto-bookmarks-boost-delete

A #fedibot that repost bookmarks 15 days after you saved it.

## Installation

```
git clone git@github.com:spinning-fantasies/masto-bookmarks-boost-delete.git
cd masto-bookmarks-boost-delete/
python3 -m venv .
source ./bin/activate
python3 -m pip install -r requirements.txt
touch .env
echo MASTODON_INSTANCE_URL={your_mastodon_instance_url} >> .env
echo MASTODON_ACCESS_TOKEN= {our_mastodon_access_token} >> .env
```




## Usage

1. Create a ``bookmarks.json`` file :

 ```
 python3 print_json.py
```

2. Loop through statuses and boost if they are 15 days old :
   
```
python3 main.py
```

4. Unbookmarks statuses :
   
```
python3 unbookmark.py
```
