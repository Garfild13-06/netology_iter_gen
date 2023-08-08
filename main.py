# Задание 1
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    def __iter__(self):
        self.result = []
        self.list_index = 0
        self.list_in_list_index = -1
        return self

    def __next__(self):
        if self.list_in_list_index >= len(self.list_of_list[self.list_index]) - 1:
            self.list_index += 1
            if self.list_index >= len(self.list_of_list):
                raise StopIteration
            self.list_in_list_index = 0
        else:
            self.list_in_list_index += 1

        item = self.list_of_list[self.list_index][self.list_in_list_index]
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # for flat_iterator_item in FlatIterator(list_of_lists_1):
    #     print(flat_iterator_item)

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Задание 2

import types


def flat_generator(list_of_lists):
    for list in list_of_lists:
        for item in list:
            yield item


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


# Задание 3
class FlatIterator_3:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    def __iter__(self):
        self.result = []
        self.list_index = 0
        self.list_in_list_index = 0
        return self

    def __next__(self):
        if self.list_in_list_index >= len(self.list_of_list[self.list_index]) - 1:
            self.list_index += 1
            if type(self.list_of_list[self.list_index][self.list_in_list_index] == 'list'):
                print("list")
            if self.list_index >= len(self.list_of_list):
                raise StopIteration
            self.list_in_list_index = 0
        else:
            self.list_in_list_index += 1

        item = self.list_of_list[self.list_index][self.list_in_list_index]
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator_3(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item, check_item)
        # assert flat_iterator_item == check_item

    # assert list(FlatIterator_3(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    # test_1()
    # test_2()
    test_3()
