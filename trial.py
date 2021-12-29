color_red = '\033[91m'
color_white = '\033[0m'

class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList():
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert_beginning(self, value):

        new_node = Node(value)
        new_node.next_node = self.head_node
        self.head_node = new_node


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
                if type(current_node.data) is str:
                    str_list += f'"{current_node.data}", '
                    current_node = current_node.next_node
                else:
                    str_list += f'{current_node.data}, '
                    current_node = current_node.next_node
            else:
                if type(current_node.data) is str:
                    str_list += f'"{current_node.data}"'
                    current_node = current_node.next_node
                else:
                    str_list += f'{current_node.data}'
                    current_node = current_node.next_node
        str_list = f'[{str_list}]'
        return str_list

    def get_length(self):
        count = 0
        node = self.head_node
        while node:
            count += 1
            node = node.next_node
        return count

    def remove_data(self, value):
        current_node = self.head_node
        try:
            if current_node.data == value:
                self.head_node = current_node.next_node
            else:
                while current_node:
                    if current_node.next_node.data != value:
                        current_node = current_node.next_node
                    else:
                        current_node.next_node = current_node.next_node.next_node
                        break
        except AttributeError:
            # raise AttributeError
            print(color_red + 'Value does not Exist!!' + color_white)


    def remove_index(self, index):
        current_node = self.head_node
        count = 0
        if index < 0 or index >= ll.get_length():
            print(color_red + 'Invalid Index Number!' + color_white)
        elif index == 0:
            self.head_node = self.head_node.next_node
        else:
            while index != count:
                count += 1
                if index == count:
                    current_node.next_node = current_node.next_node.next_node
                    break
                else:
                    current_node = current_node.next_node


    def insert_at(self, index, data):
        node = Node(data)
        current_node = self.head_node
        count = 0
        if index < 0 or index > ll.get_length():
            print(color_red + 'Invalid Index Number!' + color_white)
        elif index == 0:
            node.next_node = current_node
            self.head_node = node
        elif index == ll.get_length():
            ll.insert_end(data)

        else:
            while True:
                count += 1
                if count == index:
                    node.next_node = current_node.next_node
                    current_node.next_node = node
                    break
                else:
                    current_node = current_node.next_node

    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head_node
        node_to_insert = Node(data_to_insert)
        while True:
            if current_node.data == data_after:
                node_to_insert.next_node = current_node.next_node
                current_node.next_node = node_to_insert
                break
            else:
                current_node = current_node.next_node

    def remove_by_value(self, data):
        current_node = self.head_node
        if current_node.data == data:
            current_node = current_node.next_node
        while True:
            if current_node.next_node.data == data:
                current_node.next_node = current_node.next_node.next_node
                break
            else:
                current_node = current_node.next_node

    def swap_nodes(self, val1, val2):

        if val1 == val2:
            print('values are same!')
            return

        node1 = self.head_node
        node2 = self.head_node
        node1_prev = None
        node2_prev = None

        while True:
            if node1.data == val1:
                break
            else:
                node1_prev = node1
                node1 = node1.next_node
                if node1 is None:
                    print(color_red + 'val1 is not in the list!, execution is about to stop.' + color_white)
                    return
        while True:
            if node2.data == val2:
                break
            else:
                node2_prev = node2
                node2 = node2.next_node
                if node2 is None:
                    print(color_red + 'val2 is not in the list!, execution is about to stop' + color_white)
                    return



        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.next_node = node2

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.next_node = node1

        temp = node1.next_node
        node1.next_node = node2.next_node
        node2.next_node = temp






ll = LinkedList()
ll.insert_at(0, 15)
ll.insert_at(0, 20)
ll.insert_at(1, 'hello')
# print(ll.print_list())
ll.insert_after_value(15, 'HI')
# print(ll.print_list())

ll.insert_beginning('inanc alp')

ll.insert_after_value('HI', 27)

print(ll.print_list())

print('----------')

ll.swap_nodes(20, 15)

print(ll.print_list())

ll.swap_nodes(12, 13)

print(ll.print_list())











#
# a = Node(1)
# b = Node(2, a)
# c = Node(3, b)
# d = Node(4, c)
# ll = LinkedList(d)
#
# ll.insert_end(10)
# ll.insert_end(12)
# ll = LinkedList()
# ll.insert_at(0, 15)
# ll.insert_at(0, 20)
# ll.insert_at(1, 'hello')
# print(ll.print_list())



# print(ll.print_list())
#
# ll.insert_beginning(31)
#
# print(ll.print_list())
#
#
# items = ['inanc', 'alp', 'gunalp']
#
# for item in items:
#     ll.insert_end(item)
#
# print(ll.print_list())
#
# print(ll.get_length())
#
# ll.insert_end('sahra simay gunalp')
#
# print(ll.print_list())
#
# print('lenght:', ll.get_length())
#
# ll.remove_w_index(-1)
#
# print(ll.print_list())
#
# print('lenght:', ll.get_length())

# print('------------')
#
# print(ll.remove_data(31))
#
# print(ll.print_list())
#
#
# print(ll.remove_data('inanc'))
#
# print(ll.print_list())
#
#
# print(ll.head_node.data)
#
# print('----------')
#
# node1 = ll.head_node
#
# print(type(node1.data))
# print(node1.data)
#
# while True:
#     try:
#         if type(node1.data) is int:
#             ll.remove_data(node1.data)
#             node1 = node1.next_node
#         else:
#             node1 = node1.next_node
#     except AttributeError:
#         break
#
#
# print(ll.print_list())







