# Jhonatan Becerra

import re


def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    # check for a lowercase letter
    if re.search('[a-z]', pwd) is None:
        return False

    # check for uppercase letter
    if re.search('[A-Z]', pwd) is None:
        return False

    # check for a digit
    if re.search('[0-9]', pwd) is None:
        return False

    # check for an approved symbol
    if re.search('[~`!@#$%^&*()_+=-]', pwd) is None:
        return False

    return True