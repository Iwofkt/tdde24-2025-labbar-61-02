from books import db, pattern


def match(seq: list, pattern: list):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq

    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)

    elif not seq:
        return False

    elif pattern[0] == '&':
        print(seq[0], "== &")
        print("matching:\n", seq[1:], "\n", pattern[1:])

        return match(seq[1:], pattern[1:])

    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        print("Both are lists")
        print("matching:\n", seq[0], "\n", pattern[0])
        print("matching:\n", seq[1:], "\n", pattern[1:])

        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        print("Both are the same for:", seq[0], pattern[0])
        print("matching:\n", seq[1:], "\n", pattern[1:])
        return match(seq[1:], pattern[1:])

    return False


def search(seq, pattern):
    """
    Returns whether given sequence exists in the given pattern
    """
    if not seq:
        return match(seq, pattern)

    if match(seq, pattern):
        return True

    if isinstance(seq[0], list):
        if not isinstance(pattern[0], list):
            if search(seq[0], pattern):
                return True
        elif isinstance(pattern[0], list):
            if search(seq[0], pattern[0]):
                return True

    return search(seq[1:], pattern)


if __name__ == "__main__":
    # print(match(db, pattern))
    print("----------")
    print(search(db, [['År', 2011]])
          )
from books import db, pattern


def match(seq: list, pattern: list):
    """
    Returns whether given sequence matches the given pattern
    """
    # Base case
    if not pattern:
        # True if also empty, otherwise false
        return not seq

    elif pattern[0] == '--':
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

    elif pattern[0] == '&':
        #substitute the first element in sequence with & in pattern
        return match(seq[1:], pattern[1:])

    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])

    return False


def search(pattern: list, seq: list):
    """
    Returns all subsequences that match the given pattern
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


if __name__ == "__main__":
    print(match(db, pattern))

    print("\n----------\n ")

    # Test cases
    result1 = search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db)
    print("Result 1:", result1)

    result2 = search(['--', ['år', 2042], '--'], db)
    print("Result 2:", result2)

    result3 = search(['--', ['titel', ['&', '&']], '--'], db)
    print("Result 3:", result3)