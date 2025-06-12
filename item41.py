# yield from

def flatten_list(x):
    for num in x:
        if isinstance(num , list):
            yield from flatten_list(num)
        else:
            yield num


obj = flatten_list([1, [1, 2], 3])
print(list(obj))
def flatten_list_bad(x):
    for num in x:
        if isinstance(num , list):
            for num1 in flatten_list(num):
                yield num1
        else:
            yield num


obj = flatten_list_bad([1, [1, 2], 3])
print(list(obj))