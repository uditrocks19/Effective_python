import itertools
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

handle = open('test_file.txt')
it = index_file(handle)
results = itertools.islice(it, 0, 10)
print(results)
print(list(results))

