import types
import datetime
import os


def logger(old_function):
    path = 'main.log'

    if os.path.exists(path):
        os.remove(path)

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        sep = "||"
        log_result = f'Date & time: {datetime.datetime.now()} {sep} Function: {old_function.__name__} {sep} {args=} {sep} {kwargs=} {sep} result={result}\n'
        with open(path, 'a') as f:
            f.writelines(log_result)
        return result

    return new_function


# Задание 1
class FlatIterator_1:

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
            FlatIterator_1(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator_1(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Задание 2
def flat_generator_2(list_of_lists):
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
            flat_generator_2(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_2(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator_2(list_of_lists_1), types.GeneratorType)


@logger
# Задание 3
class FlatIterator_3:
    @logger
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    @logger
    def flatten(self, chk_list):
        result = []
        for item in chk_list:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    @logger
    def __iter__(self):
        self.result = []
        self.list_index = -1

        self.simple_list = self.flatten(self.list_of_list)
        return self

    @logger
    def __next__(self):
        if self.list_index >= len(self.simple_list) - 1:
            raise StopIteration
        else:
            self.list_index += 1
            item = self.simple_list[self.list_index]
        return item


@logger
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
        assert flat_iterator_item == check_item

    assert list(FlatIterator_3(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


@logger
def flat_generator_4(list_of_list):
    for lst in list_of_list:
        if isinstance(lst, list):
            items_lst = flatten(lst)
            for item in items_lst:
                yield item
        else:
            item = lst
            yield item


@logger
def flatten(chk_list):
    result = []
    for item in chk_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


@logger
def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_4(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        # print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(flat_generator_4(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_4(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    # test_1()
    # test_2()
    # test_3()
    test_4()
    pass
