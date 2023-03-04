# Pastebin Bisque
The Pastebin Bisque is a small Python utility that uses BeautifulSoup to scrape a user's Pastebin profile. All public pastes from that user are downloaded to disk. There is no rate-limiting protection built-in. Read about the [Pastebin Request Limits](https://pastebin.com/doc_scraping_api#2) The file name provided by the Pastebin user will be prepended with the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL fairly easy to reconstruct. 

## Quickstart
`pip install -r requirements.txt`

`python main.py -u pastebinusername`

Be sure to replace `pastebinusername` with a Pastebin username that you care about.

The files will be downloaded to the `pastes` directory in your current directory. If you searched for pastes from the user `Demonslay335`, you'd see them in the `pastes/Demonslay335` folder. 

[![asciicast](https://asciinema.org/a/564569.svg)](https://asciinema.org/a/564569)
