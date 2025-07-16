'''validate subclasses with __init_subclass__'''

class Bottle:
    def __init_subclass__(cls, **kwargs):
        print(f"Bottle.__init_subclass__ called for :{ cls.__name__}")
        if not hasattr(cls, "fill") or not callable(cls.fill):
            raise TypeError(f"{cls.__name__} must define a fill method")
        if not hasattr(cls, "show") or  not callable(cls.show):
            raise TypeError(f"{cls.__name__} must define  a show method")

class WaterBottle(Bottle):
    def __init__(self, capacity):
        self.capacity = capacity

    def fill(self):
        print(f"{self.__class__.__name__} class will fill the bottle with {self.capacity} capacity")

    def show(self):
        pass

    def __call__(self, *args, **kwargs):
        self.fill()

# obj = WaterBottle("1 litre")
# obj()

class ValidatePolygon:
    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, "side") or cls.side <3:
            raise ValueError(f" class {cls.__name__} must have an attribute with side greater than 2")

class Polygon(ValidatePolygon):
    side = 2
    pass

obj = Polygon()