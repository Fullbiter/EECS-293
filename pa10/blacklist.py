# Kevin Nash (kjn33)
# EECS 293
# Assignment 10

import re
import select
import sys


def print_blacklist(log):
    """ Print to stdout a user blacklist """

    # list to contain two dictonaries:
    #   <k,v> pairs of user and number of failed logins
    #   <k,v> pairs of user and number of illegal users
    attempts = []

    # populate attempts
    for i, line in enumerate(log):
        if "failed logins" in line.lower() or "illegal users" in line.lower():
           attempts.append(_get_attempts(log[i:]))

    # combine the two dictionaries in attempts
    attempts = _combine_dicts(attempts[0], attempts[1])
    
    # filter the dictionary into a blacklist
    deny_list = _filter_dict(attempts)

    # join all listed users into a formatted string and print
    print _join_users(deny_list)

def _get_attempts(log):
    """
    Populate a dictionary with users and a count of their bad login attempts
    """
    # regular expression for IPv4 addresses
    IP_REGEX = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    # regular expression for IPv4 addresses with known domain names
    DOMAIN_REGEX = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} \((.+?)\)"
    # regular expression for bad login counts
    COUNT_REGEX = "(\d{1,5}) time"
    
    # dictionary to populate
    attempts = dict()

    # iterate over every line in the log file following the header
    for line in log[1:]:
        # if the search finds an IP regex
        result = re.search(IP_REGEX, line)
        if result:
            user = result.group(0)
            # if the search then finds a domain name regex
            result = re.search(DOMAIN_REGEX, line)
            if result:
                user = result.group(1)
            # if the search finds a bad login regex
            result = re.search(COUNT_REGEX, line)
            if result:
                attempt_count = int(result.group(1))
                attempts[user] = attempt_count
        # if the line does not contain an IP, halt the routine
        else:
            break

    return attempts

def _combine_dicts(a, b):
    """
    Merge two dictionaries into one,
    adding together the values of key intersections
    """
    for pair in b:
        if a.get(pair):
            a[pair] += b[pair]
        else:
            a[pair] = b[pair]
    return a

def _filter_dict(log):
    """
    Create a blacklist of users whose bad
    login attempts exceed a certain threshold
    """
    threshold = _get_threshold();

    # blacklist to populate
    deny_list = []

    for key in log:
        if log[key] > threshold:
            deny_list.append(key)
    return deny_list

def _get_threshold():
    """ Parse command line arguments to obtain a security threshold """
    
    DEFAULT_THRESHOLD = 3

    # handle users passing too many arguments
    if len(sys.argv) > 2:
        raise ValueError("accepts one argument or fewer, given %d"\
                         %(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        return int(sys.argv[1])
    return DEFAULT_THRESHOLD

def _join_users(deny_list):
    """ Join the provided list into a single formatted string """
    # the number of characters remaining on the line
    remaining = 75 # 80 max - 5 spaces
    
    # the output string
    output = "     "

    for user in deny_list:
        # user is last on the line
        if remaining - (len(user) + 2) < 0:
            output = "%s,\\\n     %s" % (output, user)
            remaining = 74 - len(user)
        else:
            # non-last user is actually the first user on the line
            if output == "     ":
                output = "%s%s" % (output, user)
                remaining = remaining - len(user)
            # non-last user is in the middle of a line
            else:
                output = "%s, %s" % (output, user)
                remaining = remaining - (len(user) + 2)
    
    return output


if __name__ == "__main__":

    # stdin is not empty
    if select.select([sys.stdin,],[],[],0.0)[0]:
        # log from stdin as list of lines (strings)
        print_blacklist(sys.stdin.readlines())
    else:
        raise ValueError("stdin must have data, given none")
