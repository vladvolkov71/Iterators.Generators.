class RecursiveFlattenIterator:

    def __init__(self, array):
        self.array = iter(array)
        self.new = []

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                it = next(self.array)
                if isinstance(it, list):
                    self.new.extend(RecursiveFlattenIterator(it))
                else:
                    self.new.append(it)
            except StopIteration:
                if self.new:
                    self.new.reverse()
                    return self.new.pop()
                else:
                    raise StopIteration


def recursive_flatten_generator(arr):
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

    flat_list = RecursiveFlattenIterator(nested_list)
    print(type(flat_list))
    for item in flat_list:
        print(item)
    flat_list1 = [item for item in RecursiveFlattenIterator(nested_list)]
    print(flat_list1)

    flat_list2 = recursive_flatten_generator(nested_list)
    print(type(flat_list2))
    print(*flat_list2)
    flat_list3 = [item for item in recursive_flatten_generator(nested_list)]
    for item in flat_list3:
        print(item)
