from collections import defaultdict
class GradeSubject:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, grade):
        if name not in self._grades:
            raise ValueError(f"Student {name} not found.")
        self._grades[name][subject].append(grade)
    
    def average_grade(self, name, subject):
        if name not in self._grades or subject not in self._grades[name]:
            return 0
        grades = self._grades[name][subject]
        return sum(grades) / len(grades) if grades else 0

obj = GradeSubject()
obj.add_student("Alice")
obj.report_grade("Alice", "Math", 90)
obj.report_grade("Alice", "Math", 80)
obj.add_student("Bob")
obj.report_grade("Bob", "Science", 85)
print(obj.average_grade("Alice", "Math"))
print(obj.average_grade("Bob", "Physics")) # Should return 85.0