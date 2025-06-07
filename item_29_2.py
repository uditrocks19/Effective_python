class InputData:
    def read(self):
        raise NotImplementedError("Subclasses should implement this!")

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError("Subclasses should implement this!")

    def reduce(self, other):
        raise NotImplementedError("Subclasses should implement this!")





