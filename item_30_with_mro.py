class BaseClass:
    def __init__(self, value):
        self.value  = value

class TimesSeven(BaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNine(BaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        super().__init__(value)


    def __call__(self, *args, **kwargs):
        return self.value

obj = ThisWay(5)
print(obj())
print(ThisWay.mro())

