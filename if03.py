def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    large = a
    if large < b:
        large = b
    if large < c:
        large = c
    small = a
    if small > b:
        small = b
    if small > c:
        small = c
        
    return large, small
