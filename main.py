import argparse
import loguru
import os
import re
import shutil
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename

# BEGIN https://realpython.com/python-web-scraping-practical-introduction/
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                # loguru.logger.info("We found it.")
                return resp.content
            else:
                loguru.logger.error("Nothing happened.")
                return None

    except RequestException as e:
        loguru.logger.error("I except to that request.")
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None)
    # and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    loguru.logger.error(e)
# END https://realpython.com/python-web-scraping-practical-introduction/


def process_the_find(find):
    """
    This function takes a potential paste and assembles the raw Pastebin url.
    :param find: The string that contains a paste.
    :return: Return the full Pastebin URL and the short paste string.
    """
    the_ref = find.get('href')
    pastebin_url = "https://pastebin.com/raw" + the_ref
    loguru.logger.info(find.contents)
    find_file_name = find.contents
    return pastebin_url, the_ref, find_file_name


def get_and_save_the_paste(the_target, pastebin_url, pastebin_ref, find_file_name):
    """
    This function does the heavy listing. It does the Python equivalent of mkdir -p to prepare the environment for the
    download. The paste that has been identified is downloaded and saved to a directory that reflects the owning user.
    :param the_target: This is the user whose Pastebin profile we are looking at.
    :param pastebin_url: The full Pastebin URL.
    :param pastebin_ref: The short paste string, which is also the file name.
    :return: Nothing.
    """
    the_path = "pastes/" + the_target
    if not os.path.exists(the_path):
        os.makedirs(the_path)
    # Download the paste
    raw_html = simple_get(pastebin_url)
    # Write the paste to disk
    local_file_name = sanitize_filename(find_file_name[0])
    paste_file = the_path + pastebin_ref + "-" + local_file_name
    loguru.logger.info("Saving to {paste_file}.", paste_file=paste_file)
    with open(paste_file, 'wb') as my_file:
        my_file.write(raw_html)
    return None


def count_all_pages(div_of_pages):
    """
    Count the number of pages that this user's Pastebin account has.
    :param div_of_pages: The <div> containing the number of pages in the user's Pastebin profile
    :return: The number of pages that user's profile has.
    """
    try:
        a_tags_in_div = [tag for tag in div_of_pages[0].find_all("a")]
    except:
        number_of_pages = int()
        number_of_pages = 1
    else:
        # We used to subtract 1 because there are two links to the last page (by number and 'Oldest')
        number_of_pages = len(a_tags_in_div) 
    finally:
        loguru.logger.debug("We got through it.")

    if number_of_pages == 0:
        loguru.logger.info("OOPS.")
        number_of_pages = 1
    return number_of_pages


def parse_page_for_pastes(raw_html):
    """
    This function takes the raw HTML of a page of a user's Pastebin profile and does a lot of heavy lifting.
    Every paste on the page is found via regex, retrieved and saved to disk.
    :param raw_html: The result of a GET request.
    :return: How many pastes were saved from this page
    """
    pastes_per_page = int()
    pastes_saved = int()
    all_pastebin_urls = set()
    soup = BeautifulSoup(raw_html, 'html.parser')
    potential_pastes = [tag for tag in soup.find_all("td")]
    for i in range(len(potential_pastes)):
        pastes_per_page = pastes_per_page + 1
        the_contender = potential_pastes[i]
        potential_links = [tag for tag in the_contender.find_all("a")]
        potential_links = [link for link in potential_links if link]
        if potential_links and "archive" not in potential_links[0]['href']:
            nice_find = potential_links[0]
            pastebin_url, pastebin_ref, find_file_name = process_the_find(nice_find)
            all_pastebin_urls.add(pastebin_url)
#            save_it_as = "/" + ''.join(nice_find.contents)
            loguru.logger.info(find_file_name)
            get_and_save_the_paste(the_target, pastebin_url, pastebin_ref, find_file_name)
            pastes_saved = pastes_saved + 1
    loguru.logger.success("Turning the page.")
    return(pastes_saved)    

def count_download_all_pastes(pastebin_profile, the_target):
    """
    This function takes a Pastebin username and user profile URL as input. In return, the number of pages of pastes 
    for that user is printed. Additionally, this function calls parse_page_for_pastes() which in turn calls the 
    function that actually saves pastes from Pastebin and writes them to disk.
    :param pastebin_profile: The URL to the Pastebin user's profile.
    :param the_target: The Pastebin user that has been specified.
    :return: The total number of pastes that were saved
    """
    loguru.logger.info(pastebin_profile)
    the_hunt = simple_get(pastebin_profile)
    chowder = BeautifulSoup(the_hunt, 'html.parser')
    div_of_pages = chowder.findAll("div", {"class": "pagination"})
    number_of_pages = count_all_pages(div_of_pages)
    loguru.logger.debug(
        "TARGET ANALYZED: {the_target} has {pages} pages of pastes.", the_target=the_target, pages=number_of_pages)
    total_pastes_saved = int()
    for p in range(number_of_pages + 1):
        if p == 1:
            pastes_saved = int()
            raw_html = simple_get(pastebin_profile)
            pastes_saved = parse_page_for_pastes(raw_html)
            total_pastes_saved = pastes_saved + total_pastes_saved
        if p >= 2:
            new_case = str()
            new_case = pastebin_profile + "/" + str(p)
            raw_html = simple_get(new_case)
            try:
                pastes_saved = int()
                pastes_saved = parse_page_for_pastes(raw_html)
                total_pastes_saved = pastes_saved + total_pastes_saved
            except:
                loguru.logger.info("No other pages.")
            loguru.logger.info(new_case)
    return total_pastes_saved


def zip_the_pastes(username):
    """
    Collect the downloaded pastes into a zip file.
    """
    dir_name = "pastes/" + username
    output_filename = username
    shutil.make_archive(output_filename, 'zip', dir_name)
    

def main(the_target, to_zip):
    """
    This function accepts a username as input.
    :param the_target: Pastebin username
    :return: Absolutely nothing
    """
    loguru.logger.info(
        "PASTEBIN USER SELECTED: {the_user}", the_user=the_target)
    pastebin_profile = "https://pastebin.com/u/" + the_target
    how_many_pastes = count_download_all_pastes(pastebin_profile, the_target)
    loguru.logger.success("I downloaded {how_many_pastes} pastes.", how_many_pastes=how_many_pastes)
    if to_zip:
        loguru.logger.info("You want to zip.")
        zip_the_pastes(the_target)
    if not to_zip:
        loguru.logger.info("You do not want to zip.")
    loguru.logger.success("All done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="""Pastebin Bisque: A Pastebin User Scraper // This is a Python program that will list and retrieve the contents of 
                       all of the public pastes of the specified user. This is implemented using BeautifulSoup rather 
                       than the Pastebin API for educational purposes.""")
    parser.add_argument('--username', '-u', default="Demonslay335",
                        type=str, help="The Pastebin user you want to target")
    parser.add_argument('--zip', '-z', action='store_true', help="Use if you want to zip the results")
    args = parser.parse_args()
    the_target = args.username
    to_zip = args.zip
    main(the_target, to_zip)
