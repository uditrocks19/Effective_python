class ReadVisits:
    def __init__(self, path):
        self.data_path = path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

def check(path):
    with open(path) as f:
        for line in f:
            yield int(line)
obj = ReadVisits('test1.txt')
print(sum(check('test1.txt')))
print(sum(check('test1.txt')))