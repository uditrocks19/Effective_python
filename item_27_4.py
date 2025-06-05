from collections import defaultdict, namedtuple
Grade = namedtuple('Grade', ['score', 'weight'])

class Subject:
    def __init__(self):
        self._grades = []
    
    def report_grades(self, score, weight=1):
        self._grades.append(Grade(score, weight))
    
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight if total_weight else 0


# class to represent a set of subjects being studied by a student
class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self, name):
        total, cnt = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            cnt += 1
        return total / cnt if cnt else 0

# contaier for all students
class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
    
    def get_student(self, name):
        return self._students[name]
    
    def average_grade(self, name):
        return self._students[name].average_grade(name)

