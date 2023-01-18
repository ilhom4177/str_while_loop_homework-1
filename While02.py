def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0

    sanash = 0
    while i<len(s):
        if s[i].isalpha():
            sanash+=1 

        i=i+1
    return sanash
print(main("njn"))