def count_words(contents):
    """
    Return the number of whitespace-delimited words in the given text.
    """
    return len( contents.split() )

def count_chars(contents):
    """
    Return a dict mapping each lowercase character to its count.
    """

    char_count_dict = {}

    for char in contents.lower():
        # char_count_dict[char] = char_count_dict.setdefault(char, 0) + 1
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    return char_count_dict

def sort_dictionary( unsorted_dict ):
    """
    Takes a dictionary of the form {'a': 2, 'b': 5} and returns
    a list of dictionaries of the form
    [{'char': 'b', 'num': 5}, {'char': 'a', 'num': 2}]
    sorted by num descending.
    """

    sorted_list = [{'char': c, 'num': n} for c, n in unsorted_dict.items()]
    sorted_list.sort(key=lambda item: item['num'], reverse=True)

    return sorted_list
