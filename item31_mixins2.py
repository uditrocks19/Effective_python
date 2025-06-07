import json
class ToDictMixin:
    def to_dict(self):
        return self.__dict__

class Jsonify(ToDictMixin):
    def jsonify(self):
        return json.dumps(self.to_dict())

class User(Jsonify):
    def __init__(self, name, age):
        self._age = age
        self._name = name

user = User("Udit", 27)
print(user.to_dict())
print(user.jsonify())
