# clas simple gradebook
class Gradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        if name not in self._grades:
            return 0
        return sum(self._grades[name]) / len(self._grades[name])
    
# instance of Gradebook
g = Gradebook()
g.add_student("Alice")
g.report_grade("Alice", 90)
g.report_grade("Alice", 80)
print(g.average_grade("Alice")) # Should return 85.0
    
