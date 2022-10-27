def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer = 0
    if a > b:
        if a > c:
            answer = a
        else:
            answer = c
    else:
        if b > c:
            answer = b
        else:
            answer = c
    return answer

print(main(4,5,6))