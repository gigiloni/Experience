class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Invalid index')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise IndexError('Index must be integer and not negative')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise IndexError('Index must be integer and not negative')

        del self.marks[key]


s1 = Student('George', [1, 1, 2, 1, 2])
# print(s1.marks[2])
print(s1[2])

print(s1.marks)
#  s1.marks[2] = 1
s1[2] = 1
print(s1.marks)
s1[10] = 2
print(s1.marks)
del s1[9]
print(s1.marks)
