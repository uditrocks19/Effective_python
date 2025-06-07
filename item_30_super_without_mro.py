class BaseClass:
    def __init__(self, value):
        self.value  = value

class TimesSeven(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        self.value *= 7

class PlusNine(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

    def __call__(self, *args, **kwargs):
        return self.value

obj = ThisWay(5)
print(obj())

