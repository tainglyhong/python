def find_longest_name(names):
    """Returns the longest string in a list of names."""
    longest = ""
    for name in names:
        if len(name) > len(longest):
            longest = name

    return longest

name = find_longest_name(["logo.png", "metrics.csv", "cat.gif"])

print(name)