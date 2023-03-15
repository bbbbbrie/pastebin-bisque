# Pastebin Bisque

![GitHub last commit](https://img.shields.io/github/last-commit/bbbbbrie/pastebin-bisque)

The Pastebin Bisque is a small Python utility that uses [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) to scrape the pastes from a user's Pastebin profile. All public pastes from that user are downloaded to disk. There is no rate-limiting protection built-in. Read about the [Pastebin Request Limits](https://pastebin.com/doc_scraping_api#2) if you anticipate generating a large number of requests. The file name provided by the Pastebin user will be prepended with the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL fairly easy to reconstruct. 

## Quickstart
`pip install -r requirements.txt`

`python main.py -u pastebinusername`

Be sure to replace `pastebinusername` with a Pastebin username that you care about.

The files will be downloaded to the `pastes` directory in your current directory. If you searched for pastes from the user `Demonslay335`, you'd see them in the `pastes/Demonslay335` folder. 

[![asciicast](https://asciinema.org/a/564569.svg)](https://asciinema.org/a/564569)

### Zip the results

Use something like this:

```
python main.py --username thecutestcat --zip
```

You will find the results in `thecutestcat.zip`. 

## Help

```
usage: main.py [-h] [--username USERNAME] [--zip]

Pastebin Bisque: A Pastebin User Scraper // This is a Python program that will list and retrieve the contents of all of the public pastes of the specified user. This is implemented using BeautifulSoup rather than the Pastebin API for educational
purposes.

options:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
                        The Pastebin user you want to target
  --zip, -z             Use if you want to zip the results
  ```