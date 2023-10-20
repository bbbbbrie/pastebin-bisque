from contextlib import closing
from pathlib import Path

from requests import get

from pastebin_bisque.cli import get_and_save_the_paste
from pastebin_bisque.cli import is_good_response
from pastebin_bisque.cli import log_error
from pastebin_bisque.cli import simple_get
from pastebin_bisque.cli import zip_the_pastes


def test_count_all_pages():
    pass


def test_zip_the_pastes():
    username = "thecutestcat"
    the_path = "pastes/" + username
    the_path = Path(the_path)
    the_path.mkdir(parents=True, exist_ok=True)
    result = zip_the_pastes(username)
    assert result is None


def test_process_the_find():
    pass


def test_get_and_save_the_paste():
    pastebin_user = "thecutestcat"
    pastebin_url = "https://pastebin.com/raw/hD7ZCsNt"
    pastebin_ref = "hD7ZCsNt"
    find_file_name = "// Perform some action with the data read"
    omg = get_and_save_the_paste(pastebin_user, pastebin_url, pastebin_ref, find_file_name)
    assert omg is None


def test_log_error():
    e = "Such a cute cat."
    omg = log_error(e)
    assert omg is None


def test_simple_get():
    the_url = "https://pastebin.com/u/thecutestcat"
    simple_get(the_url)
    # pass


def test_is_good_response():
    url = "https://pastebin.com/u/thecutestcat"
    with closing(get(url, stream=True, timeout=5)) as resp:
        is_good_response(resp)
    assert resp.status_code == 200
    url = "https://pastebin.com/u/thecutestcatthatwillnevereverexistbutthisisasillytestanywaysooooooo"
    with closing(get(url, stream=True, timeout=5)) as resp:
        is_good_response(resp)
    assert resp.status_code == 404
