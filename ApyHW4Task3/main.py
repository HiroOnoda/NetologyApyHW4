class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count == len(self.list_of_list):
            raise StopIteration
        else:
            # print(len(self.list_of_list))
            if (type(self.list_of_list[self.count]) is list):
                # print(type(self.list_of_list[self.count]))
                return FlatIterator(self.list_of_list[self.count])
            else:
                # print(type(self.list_of_list[self.count]))
                self.count += 1
                item = self.list_of_list[self.count-1]
                # print(item)
                return item



def test_3():
    test_list1 = ['a', 'b', 'c',['d','D']]
    # print(list())
    # FlatIterator(test_list1)
    for item in FlatIterator(test_list1):
        print(item)
    # list_of_lists_2 = [
    #     [['a'], ['b', 'c']],
    #     ['d', 'e', [['f'], 'h'], False],
    #     [1, 2, None, [[[[['!']]]]], []]
    # ]
    #
    # for flat_iterator_item, check_item in zip(
    #         FlatIterator(list_of_lists_2),
    #         ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    # ):
    #     # print("_")
    #     print(flat_iterator_item,check_item)
    #     # assert flat_iterator_item == check_item
    #
    # assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
