import sys


class Stack:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def read(self):
        return self.elements[-1] if self.elements else None

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def is_empty(self):
        return not bool(self.elements)


numbers = [2, 1, 5, 32, 43, 12, 4, 6]
my_stack = Stack(elements=numbers)
print(my_stack.read())  
my_stack.push(element=123)
print(my_stack.read())  
print(my_stack.pop())  
print(my_stack.is_empty())  


class Bracketer:
    BRACKET_PAIRS = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def __init__(self):
        self.stack = None

    def check(self, text):
        unbalanced_found = False
        self.stack = Stack()
        for char in text:
            print(f"Processing character: {char}")
            sys.stdout.flush()
            if char in self.BRACKET_PAIRS.keys():
                self.stack.push(char)
            elif char in self.BRACKET_PAIRS.values():
                if self.stack.is_empty() or self.BRACKET_PAIRS[self.stack.pop()] != char:
                    unbalanced_found = True
                    print(f'Please check your text, you probably have no pair with {char}')
                    sys.stdout.flush()

        if unbalanced_found:
            print('Please check your text!')
            sys.stdout.flush()

        return not unbalanced_found and self.stack.is_empty()


bracketer = Bracketer()
result = bracketer.check('hey()')
result_1 = bracketer.check('hey(')
print(result)
print(result_1)
