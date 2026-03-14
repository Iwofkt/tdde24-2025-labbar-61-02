
def split_by_first(seq: list[str]):

    return_list = {}

    for word in seq:
        key = word[0]
        if key not in return_list:
            return_list[key] = [word]
        else:
            return_list[key].append(word)
    return return_list


if __name__ == "__main__":
    assert split_by_first(['apa', 'bepa', 'arg']) == {'a': ['apa', 'arg'], 'b': ['bepa']}
