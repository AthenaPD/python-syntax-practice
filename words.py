def print_upper_words(list_of_words):
    """
    For a list of words, print out each word on a separate line, but in all uppercase.

    - input: a list of strings

    For example:
    print_upper_words(["apple", "pear", "orange"]) 

    Should print: 
        APPLE
        PEAR
        ORANGE
    """

    for word in list_of_words:
        print(word.upper())


print_upper_words(["apple", "pear", "orange"])


def print_upper_words_w_e(list_of_words):
    """
    For a list of words, only prints words that start with the letter ‘e’ (either upper or lowercase), 
    but in all uppercase.

    - input: a list of strings

    For example:
    print_upper_words_w_e(["apple", "elephant apple", "pear", "orange", "eggplant"]) 

    Should print: 
        ELEPHANT APPLE
        EGGPLANT
    """

    for word in list_of_words:
        if word.lower().startswith("e"):
            print(word.upper())

print_upper_words_w_e(["apple", "elephant apple", "pear", "orange", "eggplant"])


def print_upper_words_w_lett(list_of_words, must_start_with):
    """
    For a list of words, only prints words that start with a letter specified by lett
    (either upper or lowercase), but in all uppercase.

    - list_of_words: a list of strings
    - must_start_with: a set of strings to indicate what words starting with to print

    For example:
    print_upper_words_w_lett(["apple", "elephant apple", "pear", "orange", "Peach"], {"p", "o"}) 

    Should print: 
        PEAR
        ORANGE
        PEACH
    """

    must_start_with_lower = {lett.lower() for lett in must_start_with}
    for word in list_of_words:
        if word.lower()[0] in must_start_with_lower:
            print(word.upper())

print_upper_words_w_lett(["apple", "elephant apple", "pear", "orange", "Peach"], {"p", "o"})
print_upper_words_w_lett(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
