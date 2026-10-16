def build_vocab(tokens):
    """
    Build a vocabulary dictionary from a list of tokens.

    Args:
        tokens: list of string tokens

    Returns:
        Dict mapping each unique token (sorted) to a unique integer ID starting from 0.
    """
    dictonary = {}
    tokens = list(set(tokens))
    tokens.sort()
    counter = 0
    for token in tokens:
        dictonary[token] = counter
        counter += 1
    return dictonary
