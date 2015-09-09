# Kevin Nash (kjn33)
# EECS 293
# Assignment 1

def longest_common_prefix(list_1, list_2, cpr):
    """Return the largest common prefix of argument lists in list form,
    if the first elements of list_1 and list_2 exist and are equal.
    """
    if list_1 and list_2 and cpr(list_1[0], list_2[0]):
        return [list_1[0]] + longest_common_prefix(list_1[1:], list_2[1:], cpr)
    return []



if __name__ == "__main__":
    # User enters data for both lists
    print "Input first list:"
    list_1 = input()
    print "Input second list:"
    list_2 = input()
    print('Longest common prefix:\n' +
            str(longest_common_prefix(list_1, list_2, lambda x, y : x == y)))