# masto-bookmarks-boost-delete

A #fedibot that repost bookmarks 15 days after you saved it.

## Usage

1. Create a ``bookmarks.json`` file with ``print_json.py``
2. Loop through statuses and boost if they are 15 days old
3. Unbookmarks statuses using ``unbookmark.py``
