class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.priv = new_node
            new_node.next = self.head
            self.head = new_node

dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()