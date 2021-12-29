

class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList():
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert_end(self, value):

        if self.head_node is None:
            self.head_node = Node(value)
        else:
            current_node = self.head_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = Node(value)

    def print_list(self):
        str_list = ''
        current_node = self.head_node
        while current_node is not None:
            if current_node.next_node is not None:
                str_list += f'{current_node.data}, ' #data or value?
                current_node = current_node.next_node
            else:
                str_list += f'{current_node.data}'
                current_node = current_node.next_node
        str_list = f'[{str_list}]'
        return str_list

a = Node(1)
b = Node(2, a)
c = Node(3, b)
d = Node(4, c)
ll = LinkedList(d)

ll.insert_end(10)
ll.insert_end(12)

print(ll.print_list())

