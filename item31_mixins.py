class User:
    def __init__(self,name, age):
        self._name = name
        self._age = age

class ToDictMixin:
    def to_dict(self):
        return self.__dict__

class SerializableUser(User, ToDictMixin):
    def __init__(self, name, age):
        User.__init__(self, name, age)
user = SerializableUser("Alice", 29)
print(user.to_dict())