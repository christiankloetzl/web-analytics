"""Main package from the WebAnalytics project.

Can be used as application or package.
"""

import sys
# My packages:
import utility.site


def start(url):
    """Get information from a website and print it.

    Arguments:
        url -- The requested website url
    """
    # Get comments:
    print("Comments:")
    comments = utility.site.get_comments(url)
    for comment in comments:
        print("* Comment: {0}".format(comment))
    # Get email addresses:
    print("Email addresses:")
    email_addresses = utility.site.get_email_addresses(url)
    for email_address in email_addresses:
        print("* Email: {0}".format(email_address))
    # Get links:
    print("Links:")
    links = utility.site.get_links(url)
    for link in links:
        print("* Link: {0}".format(link))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Start interactive mode
        url_path = input("URL: ")
    elif len(sys.argv) == 2:
        # Start with console arguments
        url_path = sys.argv[1]
    else:
        sys.exit("Wrong number of arguments!\nUsage: webanalytics.py <URL>")
    start(url_path)
