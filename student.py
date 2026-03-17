class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll:{self.roll}, Name:{self.name}, Marks:{self.marks}"

    def to_dict(self):
        return {
            'roll': self.roll,
            'name': self.name,
            'marks': self.marks
        }

    @classmethod
    def from_dict(cls, data): # cls = Student class itself
        return cls(data['roll'], data['name'], data['marks'])