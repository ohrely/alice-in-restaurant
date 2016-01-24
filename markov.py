import doctest


def pull_text(file_path):
    """Open and read file with source text.

    >>> pull_text("test.txt")
    'All mimsy were the borogroves\\nAnd the mome raths outgrabe. And the mome raths outgrabe.'
    """

    with open(file_path) as source_text:
        read_text = source_text.read()

    return read_text


def strip_text(text):
    """Strip odd characters from source text.

    TODO: May choose to reintroduce some of these characters later.
    TODO: Modularity!

    >>> strip_text(pull_text("test.txt"))
    ['All', 'mimsy', 'were', 'the', 'borogroves', 'And', 'the', 'mome', 'raths', 'outgrabe.', 'And', 'the', 'mome', 'raths', 'outgrabe.']
    """

    text = " ".join(text.split("\n"))
    text = " ".join(text.split("-"))
    text = text.split()

    return text


def make_chains(text):
    """Break text down into chains.  Store in dictionary.

    >>> make_chains(strip_text(pull_text("test.txt")))

    """

    chains = {}

    for i in range(len(text[:-2])):
        if (text[i], text[i + 1]) in chains:
            chains[(text[i], text[i + 1])].append(text[i + 2])
        else:
            chains[(text[i], text[i + 1])] = [text[i + 2]]

    print chains


# construct tweets - use while loop for now


if __name__ == "__main__":

    doctest.testmod(verbose=True)
