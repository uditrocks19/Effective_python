# Creating a dictionary that iterated over a dictionary in alphabetical order rathern than insertion order
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
    
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)

a = SortedDict()
a['alligator'] = 'hatchling'
a['dog'] = 'puppy'
a['cow'] = 'calf'

class MissingDict(dict):
    def __missing__(self, key):
        print(f"Missing: {key}")
        print(f"adding default value 0 for {key}")
        self[key] = 2
        return 2

a = MissingDict()
a['alligator'] = 1
a['dog'] = 2 
ans = {"dog":2, "hen": 10}
for key, value in ans.items():
    a[key] += value 
print(a.items())