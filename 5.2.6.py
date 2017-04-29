def parse_int(string):
    while 1:
        try:
            string = int(string)
        except ValueError:
            print('Value should be integer! Try again:')
            string = input()
        else:
            return string


class Node:
    def __init__(self, value, next_element):
        self.value = value
        self.next_element = next_element


class Ring:
    def __init__(self):
        self.current = None
        self.size = 0

    def make_ring(self, n):
        self.size = n
        for i in range(n):
            print('Input element of ring')
            if self.current is None:
                self.current = Node(parse_int(input()), None)
                self.current.next_element = self.current
            else:
                self.current.next_element = Node(parse_int(input()), self.current.next_element)
                self.current = self.current.next_element
        self.current = self.current.next_element

    def __str__(self):
        if self.current is not None:
            out = str(self.current.value) + ' '
            for i in range(self.size-1):
                self.current = self.current.next_element
                out += str(self.current.value) + ' '
            self.current = self.current.next_element
            return out
        return 'None'


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if value > self.value:
                    if self.right is None:
                        self.right = TreeNode(value)
                    else:
                        self.right.insert(value)

    def print_path(self):
        right_path = []
        left_path = []
        if self is None:
            return []
        if self.right is None and self.left is None:
            return [self.value]
        if self.right is not None:
            right_path = [self.value] + self.right.print_path()
        if self.left is not None:
            left_path = [self.value] + self.left.print_path()
        return compare_length(right_path, left_path)


class Tree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, data):
        self.root.insert(data)


def from_ring_to_tree(ring, tree):
    for i in range(ring.size):
        tree.insert(ring.current.value)
        ring.current = ring.current.next_element


def compare_length(list1, list2):
    return list1 if len(list1) > len(list2) else list2


main_tree = Tree()
main_ring = Ring()

print('How much elements will be in ring?')
elements_in_ring = parse_int(input())
main_ring.make_ring(elements_in_ring)

from_ring_to_tree(main_ring, main_tree)
print('the longest branch is:', main_tree.root.print_path())


