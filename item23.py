from collections import defaultdict
class MyClass:
    def __init__(self):
        self.alligator = "hatchling"
        self.cow = "calf"
    
    def __repr__(self):
        return f"MyClass(alligator={self.alligator!r}, cow={self.cow!r})"
    

a = MyClass()
for key, value in a.__dict__.items():
    print(f"{key}: {value}")
print(a)