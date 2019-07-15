"""Provides functions for getting information from websites."""

import urllib.request
import urllib.error
# My packages:
import utility.parser


def get_html(url):
    """Request a website and return the html as a string.

    Arguments:
        url -- The requested website url.
    """
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        return str(html)
    except urllib.error.HTTPError as e:
        print(' * The server couldn\'t fulfill the request.')
        print(' * Error code: ', e.code)
    except urllib.error.URLError as e:
        print(' * The server couldn\'t be reached.')
        print(' * Reason: ', e.reason)


def get_corefile(url):
    """Request a corefile and return it as a string.

    Arguments:
        url -- The requested website url.
    """
    corefile = get_html(url + "/core")
    return corefile


def get_comments(url):
    """Request an url, parse all the comments and return them as a list.

    Arguments:
        url -- The requested website url.
    """
    html = get_html(url)
    html_parser = utility.parser.CommentParser()
    html_parser.feed(html)
    return html_parser.get_comments()


def get_email_addresses(url):
    """Request an url, parse all the email addresses and return them as a list.

    Arguments:
        url -- The requested website url.
    """
    html = get_html(url)
    email_parser = utility.parser.EmailAddressParser()
    email_parser.feed(html)
    return email_parser.get_email_addresses()


def get_links(url):
    """Request an url, parse all the links and return them as a list.

    Arguments:
        url -- The requested website url.
    """
    html = get_html(url)
    link_parser = utility.parser.LinkParser()
    link_parser.feed(html)
    return link_parser.get_links()
