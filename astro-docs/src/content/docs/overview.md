---
title: 🗂️ Overview
---

The Pastebin Bisque is a small Python utility that uses BeautifulSoup to scrape a user's [Pastebin](https://pastebin.com/) profile. All public pastes from that user are downloaded to disk. Optionally, the pastes can be saved to a single `.zip` file.

There is no rate-limiting protection built-in. Read about the [Pastebin Request Limits](https://pastebin.com/doc_scraping_api#2) if you anticipate generating a large number of requests. The file name provided by the Pastebin user will be prepended with the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL fairly easy to reconstruct.

TL;DR - Scrape all public Pastebin pastes from a user.

Free software: GNU Lesser General Public License v3 or later (LGPLv3+)