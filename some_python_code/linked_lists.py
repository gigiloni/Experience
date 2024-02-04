class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:  # проверка того, есть ли у текущего узла следующий
                current_node = current_node.next_node
            current_node.next_node = new_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.data
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.display()

linked_list.remove(3)
linked_list.display()
