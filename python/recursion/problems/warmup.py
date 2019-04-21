def cumulative_sum(n: int) -> int:
    """
    Find the cumulative sum from 0 to n

    Arguments:
        n {int} -- max of cumulative sum

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
        return 0
    else:
        return n * cumulative_sum(n - 1)


def sum_func(n: int) -> int:
    """
    Add up all individual elements of a number. For example:
    sum_func(21) = 2 + 1 = 3
    sum_func(321) = 3 + 2 + 1 = 6

    Arguments:
        n {int} -- number to sum inidividual elements

    Returns:
        int -- answer
    """

    if len(str(n)) == 1:
        return n

    else:
        return n % 10 + sum_func(n // 10)


def word_split(phrase: str, list_of_words: list, output=None) -> list:
    """
    Take in a string and a list of possible words and return
    all words in the string that are in the list

    Arguments:
        phrase {str} -- string to search for words
        list_of_words {list} -- target words
        output {list} -- used in recursive calls only. DO NOT ADD PARAMETER.

    Returns:
        list -- words found in phrase
    """

    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output
