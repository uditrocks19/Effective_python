from collections import defaultdict
class GradeSubject:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, grade, weight=1):
        if name not in self._grades:
            raise ValueError(f"Student {name} not found.")
        self._grades[name][subject].append((grade, weight))
    
    def average_grade(self, name, subject):
        if name not in self._grades or subject not in self._grades[name]:
            return 0
        grades = self._grades[name][subject]
        return sum(grade * weight for grade, weight in grades) / sum(weight for _, weight in grades) if grades else 0

obj = GradeSubject()
obj.add_student("Alice")
obj.report_grade("Alice", "Math", 90, 0.5)
obj.report_grade("Alice", "Math", 80, 0.9)
obj.add_student("Bob")
obj.report_grade("Bob", "Science", 85)
print(obj.average_grade("Alice", "Math"))
print(obj.average_grade("Bob", "Physics")) # Should return 85.0