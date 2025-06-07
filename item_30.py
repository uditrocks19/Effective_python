class BaseValue:
    def __init__(self, value):
        self.value = value

class PlusOne(BaseValue):
    def __init__(self, value):
        self.value +=1

class MulTwo(BaseValue):
    def __init__(self, value):
        self.value *= 2

class Calculate(PlusOne, MulTwo):
    def __init__(self, value):
        BaseValue.__init__(self, value)
        PlusOne.__init__(self, value)
        MulTwo.__init__(self, value)
obj = Calculate(5)
print(obj.value)
