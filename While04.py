def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0

    sanash = 0
    while i<len(s):
        if s[i].isupper():
            sanash+=1 

        i=i+1
    return sanash
print(main('Codeschool'))