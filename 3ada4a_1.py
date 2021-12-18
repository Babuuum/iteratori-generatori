class iterator:
    def __init__(self, list):
        self.list = list
        self.step = 0
        self.ultra_step = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == len(self.list[self.ultra_step]):
            self.ultra_step += 1
            self.step = 0
        if self.ultra_step == len(self.list):
            raise StopIteration
        self.part = self.list[self.ultra_step][self.step]
        self.step += 1
        return self.part


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
FlatIterator = iterator

for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)