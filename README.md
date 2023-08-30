# masto-bookmarks-boost-delete

A #fedibot that repost bookmarks 15 days after you saved it.

## Installation

Clone the repository :
```
git clone git@github.com:spinning-fantasies/masto-bookmarks-boost-delete.git
```

Activate a virtualenv :

```
cd masto-bookmarks-boost-delete/
python -m venv .
source ./bin/activate
```
Install the dependencies :

```
python -m pip install -r requirements.txt
```

Add environment variables :

```
touch .env
echo MASTODON_INSTANCE_URL={your_mastodon_instance_url} >> .env
echo MASTODON_ACCESS_TOKEN= {our_mastodon_access_token} >> .env
```

## Usage

1. Create a ``bookmarks.json`` file :

 ```
 python print_json.py
```

2. Loop through statuses and boost if they are 15 days old :
   
```
python main.py
```

4. Unbookmarks statuses :
   
```
python unbookmark.py
```
