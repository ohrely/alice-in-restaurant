import doctest


def pull_text(file_path):
    """Open and read file with source text.

    >>> pull_text("test.txt")
    'All mimsy were the borogroves\\nAnd the mome raths outgrabe.'
    """

    with open(file_path) as source_text:
        read_text = source_text.read()

    return read_text


def strip_text(text):
    """Strip odd characters from source text.

    TODO: May choose to reintroduce some of these characters later.
    TODO: Modularity!

    >>> strip_text(pull_text("test.txt"))
    'All mimsy were the borogroves And the mome raths outgrabe.'
    """

    text = " ".join(text.split("\n"))
    text = " ".join(text.split("-"))

    return text


# break down into chains, store in dictionary


# construct tweets - use while loop for now


if __name__ == "__main__":

    doctest.testmod(verbose=True)
