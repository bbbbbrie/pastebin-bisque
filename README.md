# Pastebin Bisque
The Pastebin Bisque is a small Python utility that uses BeautifulSoup to scrape a user's Pastebin profile. All public pastes from that user are downloaded to disk. There is no rate-limiting. The file name provided by the Pastebin user will be ignored in favor of the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL easy to reconstruct. 

## Quickstart
`pip install -r requirements.txt`

`python main.py -u pastebinusername`

Be sure to replace `pastebinusername` with a Pastebin username that you care about.

[![asciicast](https://asciinema.org/a/306382.svg)](https://asciinema.org/a/306382)