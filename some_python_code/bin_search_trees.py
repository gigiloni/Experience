import hashlib


class Node:
    def __init__(self, left_child=None, right_child=None, value=None):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value


class Tree:
    def __init__(self, root_value):
        self.root = Node(value=root_value)

    def insert(self, value, node=None):
        if node is None:
            node = self.root

        if value == node.value:
            return

        if value < node.value:
            if node.left_child:
                self.insert(value, node.left_child)
            else:
                node.left_child = Node(value=value)
        elif value > node.value:
            if node.right_child:
                self.insert(value, node.right_child)
            else:
                node.right_child = Node(value=value)

    def search(self, value, node=None):
        if node is None:
            node = self.root

        if not node:
            return

        if node.value == value:
            return value

        if value < node.value:
            return self.search(value=value, node=node.left_child)

        if value > node.value:
            return self.search(value=value, node=node.right_child)

    def delete(self, value, node=None):
        if node is None:
            node = self.root

        if not node:
            return

        if value < node.value:
            node.left_child = self.delete(value=value, node=node.left_child)
            return node
        elif value > node.value:
            node.right_child = self.delete(value=value, node=node.right_child)
            return node
        elif node.left_child is None:
            return node.right_child
        else:
            node.right_child.lift(node.right_child, node)
            return node

    def lift(self, node, node_to_delete):
        if node.left_child:
            node.left_child = self.lift(node=node.left_child, node_to_delete=node_to_delete)
            return node
        else:
            node_to_delete.value = node.value
            return node.right_child

    def in_order_traversal(self, node=None, result=None):
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node.left_child:
            self.in_order_traversal(node=node.left_child, result=result)

        result.append(node.value)

        if node.right_child:
            self.in_order_traversal(node=node.right_child, result=result)

        return result


tree = Tree(root_value=42)
tree.insert(20)
tree.insert(37)
tree.insert(38)
tree.insert(100)
tree.insert(98)
tree.insert(99)
tree.insert(156)
tree.insert(101)

result = tree.in_order_traversal()
print(result)
print(tree.search(value=100))
tree.delete(20)
result_after_delete = tree.in_order_traversal()
print(result_after_delete)


class Book:
    def __init__(self, uid=None, title=None):
        self.title = title
        self.uid = uid
        self.uid = int(hashlib.sha256(title.encode()).hexdigest(), 16)  # creating a hash object by title

    """
        def comparing_books(self, other_book):
        if self.uid > other_book.uid:
            return 1
        if self.uid < other_book.uid:
            return -1
        else:
            return 0
    """

    def __lt__(self, other_book):
        return self.uid < other_book.uid

    def __gt__(self, other_book):
        return self.uid > other_book.uid

    def __eq__(self, other_book):
        return self.uid == other_book.uid


b1 = Book(title='War and Peace')
b2 = Book(title='Alice in Wonderland')
b3 = Book(title='One Hundred Years of Solitude')
b4 = Book(title='The Martian Chronicles')
b5 = Book(title='The Sea-Wolf')
b6 = Book(title='The Adventures of Tom Sawyer')

tree_books = Tree(root_value=b1)
tree_books.insert(b2)
tree_books.insert(b3)
tree_books.insert(b4)
tree_books.insert(b5)
tree_books.insert(b6)

result_books = tree_books.in_order_traversal()
for book in result_books:
    print(book.title)

print('======')

searched_book = tree_books.search(b6).title
print(searched_book)

print('======')

deleted_book = tree_books.delete(b4)
result_books_new = tree_books.in_order_traversal()
for book in result_books_new:
    print(book.title)
