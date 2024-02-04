class Node:
    def __init__(self):
        self.children = {}

    def __repr__(self):
        return f'Node(children={self.children})'


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]

    def search(self, word):
        current_node = self.root
        for char in word:
            children = current_node.children
            if char not in children:
                return False
            current_node = children[char]
        return True

    def autocomplete(self, prefix):
        current_node = self.root
        for char in prefix:
            children = current_node.children
            if char not in children:
                return []
            current_node = children[char]

        return self.all_words_at(node=current_node, prefix=prefix)

    def all_words_at(self, node, word='', words=None, prefix=''):
        if words is None:
            words = []

        for key, child_node in node.children.items():
            if key is None:
                words.append(prefix + word)
            else:
                self.all_words_at(node=child_node, word=word + key, words=words, prefix=prefix)
        if not node.children:
            words.append((prefix + word))

        return words

    def insert_word(self, word):
        current_node = self.root
        for char in word:
            children = current_node.children
            if char not in children:
                children[char] = Node()
            current_node = children[char]
        return current_node


trie = Trie()
trie.insert('cat')
trie.insert('bat')
trie.insert('car')

print(trie.root)
print(trie.search('cat'))
autocomplete_results = trie.autocomplete('ca')
print(autocomplete_results)
