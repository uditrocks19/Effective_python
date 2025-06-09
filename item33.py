# Create your own custom list
class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts
MyList = FrequencyList(["1", "2", "3", "6"])
print(f"the first element is {MyList[0]}")
print(MyList.frequency())


