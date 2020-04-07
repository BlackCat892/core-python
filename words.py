"""Retrieve and print words from a URL.
Usage:
    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.
    Returns:
        A list of strings containing the words from
        the document.
    """
    try:
        with urlopen(url) as story:
            story_words = []
            for line in story:
                line_words = line.decode('utf-8').split()
                for word in line_words:
                    story_words.append(word)
        return story_words

    except Exception as err:
        print(err)


def print_items(items):
    """Print items one per line.
    Args:
        An iterable series of printable items.
    """
    try:
        for item in items:
            print(item)

    except Exception as err:
        print(err)


def main(url):
    """Print each word from a text document from a URL.
    Args:
        url: The URL of a UTF-8 text document.
    """
    try:
        words = fetch_words(url)
        print_items(words)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    try:
        main(sys.argv[1])  # The 0th arg is the module filename
    except Exception as error:
        print(error)


""" def nth_root(radicand, n):
	return radicand ** (1/n) """
