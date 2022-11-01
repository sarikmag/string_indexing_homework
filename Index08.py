def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.find("*")>0:
        return s.find("*")
    return False
print(main("wde*4e"))
        