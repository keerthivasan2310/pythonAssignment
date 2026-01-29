import re

def is_valid_email(email):
    """
    Validates an email address based on specific HackerRank rules:
    - Format: username@websitename.extension
    - Username: letters, digits, dashes, and underscores
    - Website: letters and digits
    - Extension: letters only, max length 3
    """
    # Regex breakdown:
    # ^[a-zA-Z0-9_-]+   : Username (letters, numbers, -, _)
    # @[a-zA-Z0-9]+     : @ followed by Website name (letters, numbers)
    # \.[a-zA-Z]{1,3}$  : . followed by Extension (letters only, length 1-3)
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))

def filter_emails(emails):
    """
    Filters a list of emails and returns valid ones in lexicographical order.
    """
    valid_emails = list(filter(is_valid_email, emails))
    valid_emails.sort()
    return valid_emails