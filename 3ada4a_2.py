#def flat_generator(list):
    #step = 0
    #ultra_step = 0
    #end = 0
    #end_2 = 0
    #for search in list:
        #end += len(search)
    #while end_2 != end:
        #if step  == len(list[ultra_step]):
            #ultra_step += 1
            #step = 0
        #part_of_list = list[ultra_step][step]
        #step += 1
        #end_2 += 1
        #yield part_of_list

def flat_generator(list):
    for search in list:
        for search_2 in search:
            part = search_2
            yield part

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

for item in  flat_generator(nested_list):
    print(item)
flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)