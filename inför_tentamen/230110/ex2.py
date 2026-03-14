def split_lists(seq: list, sizes: str):

    seq_copy = seq.copy()
    size: int = 0
    return_list: list[list[int]] = []
    internal_list = []

    for number in sizes:
        value = int(number)
        size += value

        for i in range(value):
            internal_list.append(seq_copy.pop(0))
        return_list.append(internal_list)
        internal_list = []

    if size != len(seq):
        raise ValueError
    return return_list


def split_lists_rec(seq: list, sizes: str):
    if seq == []:
        if sizes == []:
            return []
        raise ValueError
    return_list = []
    return_list.append(split_lists_rec(seq[1:], sizes[1:]))

    return return_list


assert split_lists_rec([1, 2, 0, 4, 7, 6], "132") == [[1], [2, 0, 4], [7, 6]]
