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

    else:
        return False


if __name__ == "__main__":
    print(match(db, pattern))
