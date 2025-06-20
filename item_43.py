import itertools
# chaining iterators
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))
# repeat
it = itertools.repeat('hello', 3)
print(list(it))
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))
# zip_longest
key = [1, 2, 3]
value = ["apple", "oranges"]
for key, value in itertools.zip_longest(key, value, fillvalue='lemon'):
    print(key, value, sep = '\t')
# islice itertools
values = [1, 2, 3, 5, 10, 13]
first_five = itertools.islice(values, 5)
print(list(first_five))
# itertools takewhile
values = [ 4, 5 , 9,  2]
less_than_7 = lambda x : x < 7
it = itertools.takewhile(less_than_7, values)
print(list(it))

# itertools accumulate running total
values = [i for i  in range(1, 11)]
sum_reduce = itertools.accumulate(values)
print(list(sum_reduce))
# pass a function
def sum_modulo_20(first, second):
    output = first + second
    return output % 20
sum_reduce_by_function = itertools.accumulate(values, sum_modulo_20)
print(list(sum_reduce_by_function))

# itertools.permutations
it = itertools.permutations(values)
print(next(it))
print(next(it))

# itertools combinations
# unordered set
it = itertools.combinations(values, 2)
print(list(it))
