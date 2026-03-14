def match(seq: list, pattern: list):
    """
    Returns whether a sequence matches the pattern
    """
    # Base case
    if not pattern:
        # True if also empty, otherwise false
        return not seq

    elif pattern[0] == "--":
        # Try match sequence with pattern - first element
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        # If match(seq, pattern[1:]) doesnt work we
        # instead try to make '--' "cover" more of the sequence
        else:
            return match(seq[1:], pattern)

    # if we have a pattern that isn't empty, and it
    # doesn't contain '--' while sequence is empty
    # they cant match
    elif not seq:
        return False

    elif pattern[0] == "&":
        # substitute the first element in sequence with & in pattern
        return match(seq[1:], pattern[1:])

    # Add functionality to match nestled lists.
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])

    return False


def search(pattern: list, seq: list):
    """
    Returns a list of all elements in a sequence that match the pattern
    """

    # Find all elements in sequence that match the pattern
    result = []
    for element in seq:
        if match(element, pattern):
            result.append(element)

    return result


# -- EXTRA -- #


def deep_search(pattern: list, seq: list):
    """
    Returns a list of all subsequences in a sequence that match the pattern
    """
    results = []

    # Base case: if sequence is empty
    if not seq:
        if match(seq, pattern):
            return [seq]
        else:
            return []

    # Check if current sequence matches the pattern
    if match(seq, pattern):
        results.append(seq)

    # If current element is a list, search within it
    if isinstance(seq[0], list):
        sub_results = search(pattern, seq[0])
        results.extend(sub_results)

    # Continue searching in the rest of the sequence
    rest_results = search(pattern, seq[1:])
    results.extend(rest_results)

    return results
