from collections import defaultdict
class CountMising:
    def __init__(self):
        self.value = 0
    
    def __call__(self):
        self.value += 1
        return 0

assert callable(CountMising) # Check if CountMising is callable
increments = {
    'a':1,
    'b':2,
    'c':3
}
obj = CountMising()
dct = defaultdict(obj)
for key, value in increments.items():
    dct[key] += value
print(dct.items())
print(obj.value)