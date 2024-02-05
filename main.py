from typing import Iterable


def recursive_flatten_iterator(array: Iterable):
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(recursive_flatten_iterator(i))
        else:
            lst.append(i)
    return iter(lst)


def recursive_flatten_generator(arr: Iterable):
    for i in arr:
        if isinstance(i, list):
            yield from recursive_flatten_generator(i)
        else:
            yield i


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', [1, [4, 5, 6], 2, 3], 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    flat_list = recursive_flatten_iterator(nested_list)
    print(type(flat_list))
    for item in flat_list:
        print(item)
    flat_list1 = [item for item in recursive_flatten_iterator(nested_list)]
    print(flat_list1)

    flat_list2 = recursive_flatten_generator(nested_list)
    print(type(flat_list2))
    print(*flat_list2)
    flat_list3 = [item for item in recursive_flatten_generator(nested_list)]
    for item in flat_list3:
        print(item)
