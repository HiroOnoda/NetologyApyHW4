class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.in_count = 0
        self.out_count = 0
        return self

    def __next__(self):
        if self.out_count == len(self.list_of_list):
            raise StopIteration
        else:
            if self.in_count == len(self.list_of_list[self.out_count]):
                self.in_count = 0
                self.out_count += 1
                item = self.list_of_list[self.out_count][self.in_count]
                self.in_count += 1
            else:
                item = self.list_of_list[self.out_count][self.in_count]
                self.in_count += 1
            print(item)
            return item




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
        print()
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()