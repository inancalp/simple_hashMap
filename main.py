class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList():
    def __init__(self, head_node=None):
        self.head_node = head_node


class HashTable():
    def __init__(self):
        self.max = 10
        self.array = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max

    def add(self, key, value):
        if not self.array[self.get_hash(key)]:
            try:
                h = self.get_hash(key)
                while True:
                    if self.array[h] is None:
                        self.array[h] = value
                        break
                    else:
                        h = h + 1
            except IndexError:
                h = 0
                while True:
                    if self.array[h] is None:
                        self.array[h] = value
                        break
                    else:
                        h = h + 1
        else:
            print('''
----------------------
KEY is already taken!!
----------------------
''')



    def get_value(self, key):
        h = self.get_hash(key)
        return self.array[h]


print(ord('m'))

ht = HashTable()
print('hash num "m":', ht.get_hash('m'))
ht.add('m', 'HELLO')
ht.add('m', 'Hi')
print(ht.array)
print(ht.get_value('m'))
print(ht.get_value('m'))
# l = [1, 2, 3, 4]
#
# print(l[4])


# try:
#     h = self.get_hash(key)
#     while self.array[h]:
#         h = h + 1
#         if self.array[h] is None:
#             self.array[h] = value
#             break
#         else:
#             continue
# except IndexError:
#     h = 0
#     while self.array[h]:
#         h = h + 1
#         if self.array[h] is None:
#             self.array[h] = value
#             break
#         else:
#             continue