"""Contains parser classes for html tags and comments."""

import html.parser
import html.entities
import urllib.parse


class AbstractParser(html.parser.HTMLParser):
    """Dummy class for overwriting the error() method."""

    def __init__(self):
        super(AbstractParser, self).__init__()

    def error(self, message):
        pass


class CommentParser(AbstractParser):
    """Class for getting comments parsed from HTML."""

    def __init__(self):
        super(CommentParser, self).__init__()
        self.__comments = []

    def handle_comment(self, comment):
        """Append comments to comment list.

        Arguments:
            comment -- The parsed comment.
        """
        self.__comments.append(comment)

    def get_comments(self):
        """Return the comments as a list."""
        return self.__comments


class EmailAddressParser(AbstractParser):
    """Class for getting email addresses parsed from HTML."""

    def __init__(self):
        super(EmailAddressParser, self).__init__()
        self.__email_addresses = []

    def handle_starttag(self, tag, attributes):
        """Append mailto links (email addresses) from the href attribute to the email address list.

        Arguments:
            tag -- the parsed tag.
            attributes -- the attributes from the parsed tag.
        """
        for attribute in attributes:
            if attribute[0] == "href":
                parsed_url = urllib.parse.urlparse(attribute[1])
                if parsed_url.scheme == 'mailto':
                    self.__email_addresses.append(parsed_url.path)

    def get_email_addresses(self):
        """Return the email addresses as a list."""
        return self.__email_addresses


class LinkParser(AbstractParser):
    """Class for getting links parsed from HTML."""

    def __init__(self):
        super(LinkParser, self).__init__()
        self.__links = []

    def handle_starttag(self, tag, attributes):
        """Append href or src attributes to the link list.

        Arguments:
            tag -- the parsed tag.
            attributes -- the attributes from the parsed tag.
        """
        for attribute in attributes:
            # Get links from src or href attributes.
            if attribute[0] == "src" or attribute[0] == "href":
                # https://docs.python.org/3/library/urllib.parse.html
                parsed_url = urllib.parse.urlparse(attribute[1])
                # mailto links should not be collected.
                if parsed_url.scheme != "mailto":
                    self.__links.append("{0}{1}".format(parsed_url.netloc, parsed_url.path))

    def get_links(self):
        """Return the links as a list."""
        return self.__links
