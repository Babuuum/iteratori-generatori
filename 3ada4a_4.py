
def flat_generator(_list):
    for item in _list:
        if type(item) != list:
            yield item
        else:
            for item_2 in flat_generator(item):
                yield item_2




nested_list = ["a",
	['a',[ 'b',[ 'c']]],
	['d', ['e'], 'f'],
	[[1, 2], None],
]

for item in  flat_generator(nested_list):
    print(item)
flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)