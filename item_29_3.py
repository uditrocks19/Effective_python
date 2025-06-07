class InputData:
    @classmethod
    def generate_inputs(cls, config):
        for path in config['input_paths']:
            yield cls(path)

class PathInputData(InputData):
    def __init__(self, path):
        self.path = path

    def read(self):
        return f"Reading from: {self.path}"
config = {'input_paths' : ["test1.txt", "test2.txt"]}
for input_data in PathInputData.generate_inputs(config):
    print(input_data)
    print(input_data.read())
