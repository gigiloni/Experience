from collections import deque


class LinkedList:
    def __init__(self):
        self.linked_list = deque()

    def is_empty(self):
        return len(self.linked_list) == 0

    def append(self, data):
        self.linked_list.append(data)

    def display(self):
        print(" -> ".join(map(str, self.linked_list)))


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
