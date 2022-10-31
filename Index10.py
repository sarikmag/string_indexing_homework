def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    z=s[0]
    z=int(z)
    x=s[1]
    x=int(x)
    c=s[2]
    c=int(c)
    v=s[3]
    v=int(v)
    b=s[4]
    b=int(b)
    return int(z)+int(x)+int(c)+int(v)+int(b)
print(main("10002"))