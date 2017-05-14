class Node:
    def __init__(self, user=None, next_el=None, prev=None):
        self.data = user
        self.next = next_el
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, data):
        new_node = Node(data, None, None)
        self.length += 1
        if self.first is None:
            self.first = self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def delete_num(self, num):
        count = 0
        current_node = self.first
        while count < self.length:
            if count == num:
                if self.length - 1 == num:
                    self.last = self.last.prev
                    self.last.next = None
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.first = current_node.next
                    current_node.next.prev = None
                break
            count += 1
            current_node = current_node.next

    def delete(self, data):
        count = 0
        current_node = self.first
        if self.last.data == data:
            self.delete_num(self.length-1)
            return
        while count < self.length - 1 and current_node.data != data:
            current_node = current_node.next
            count += 1
        if self.last.data != data and self.length == count + 1:
            return
        self.delete_num(count)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [ ' + str(current.data) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.data) + ' '
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()
