import twitter
import os
import doctest
from random import choice


def pull_text(filenames):
    """Open and read file with source text.

    >>> pull_text(["test.txt"])
    'All mimsy were the borogroves\\nAnd the mome raths outgrabe. And the mome raths outgrabe.'
    """

    text = ""

    for filename in filenames:
        source_text = open(filename)
        text = text + source_text.read()

    return text


def strip_text(text):
    """Strip odd characters from source text.

    TODO: May choose to reintroduce some of these characters later.
    TODO: Modularity!

    >>> strip_text(pull_text(["test.txt"]))
    ['All', 'mimsy', 'were', 'the', 'borogroves', 'And', 'the', 'mome', 'raths', 'outgrabe.', 'And', 'the', 'mome', 'raths', 'outgrabe.']
    """

    text = "".join(text.split("("))
    text = "".join(text.split(")"))
    text = " ".join(text.split("\n"))
    text = " ".join(text.split("-"))
    text = text.split()

    return text


def make_chains(text):
    """Break text down into chains.  Store in dictionary.
    """

    chains = {}

    for i in range(len(text[:-2])):
        if (text[i], text[i + 1]) in chains:
            chains[(text[i], text[i + 1])].append(text[i + 2])
        else:
            chains[(text[i], text[i + 1])] = [text[i + 2]]

    return chains


def construct_tweet(chains):
    """Use dictionary of chains to construct new tweets.
    """

    first_key = choice(chains.keys())
    new_key = first_key

    tweet = [first_key[0], first_key[1]]

    while new_key in chains and len(tweet) < 15:
        next_word = choice(chains[new_key])
        tweet.append(next_word)
        new_key = (tweet[-2], tweet[-1])

    tweet = " ".join(tweet)

    return tweet


if __name__ == "__main__":

    doctest.testmod(verbose=True)

    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # print api.VerifyCredentials()

    corpus = pull_text(["restaurant.txt", "wonderland.txt"])
    stripped = strip_text(corpus)
    chains = make_chains(stripped)
    tweet = construct_tweet(chains)

    status = api.PostUpdate(tweet)
    print status.text
