class InputData:
    def read(self):
        raise NotImplementedError("Subclasses should implement this!")

class PathInputData(InputData):
    def __init__(self, path):
        self.path = path


obj = PathInputData("data.txt")
obj.read()