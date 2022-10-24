def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    if len(a):
        c = a==b
        c = True
    if len(a):
        c = a!=b
        c = False

    return c

print(main("hello", "hello"))     