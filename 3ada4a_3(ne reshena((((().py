class iterator:
    def __init__(self, _list):
        self.list = _list
        self.step = 0
        self.cache = cheaty(_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.cache) == self.step:
            raise StopIteration
        else:
            self.result = self.cache[self.step]
            self.step += 1
            return self.result

def cheaty (_list):
    cache = []
    for item in  cheat(_list):
        cache.append(item)
    return cache

def cheat(_list):
    for item in _list:
        if type(item) != list:
            yield item
        else:
            for item_2 in cheat(item):
                yield item_2


nested_list = ["a",
	['a',[ 'b',[ 'c']]],
	['d', ['e'], 'f'],
	[[1, 2], None],
]
FlatIterator = iterator

for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)