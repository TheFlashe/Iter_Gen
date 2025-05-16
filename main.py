import types


def flat_generator(list_of_lists):
    for lst in list_of_lists:
        for l in lst:
            yield l


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.inner_lst = 0
        self.outer_lst = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_lst < len(self.list_of_list):
            if self.inner_lst < len(self.list_of_list[self.outer_lst]):
                item = self.list_of_list[self.outer_lst][self.inner_lst]
                self.inner_lst += 1
                return item
            else:
                self.outer_lst += 1
                self.inner_lst = 0

        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
