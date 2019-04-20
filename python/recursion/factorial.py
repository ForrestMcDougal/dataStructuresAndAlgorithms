def factorial(n: int) -> int:
    """
    Find the factorial of n

    Arguments:
        n {int} -- factorial to be taken

    Returns:
        int -- answer
    """

    # error handling
    if n < 0:
        raise ValueError('n must be greater than 1')
    if type(n) != int:
        raise TypeError('n must be an integer')

    # handle base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
