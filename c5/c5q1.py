class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        print(" -> ".join(values))

inp = input("Enter Commands: ").split()

theList = LinkedList()

for i in range(0,len(inp),2):
    command = inp[i]
    if command == "append":
        theList.append(inp[i+1])
    elif command == "insert_head":
        theList.insert_head(inp[i+1])
    elif command == "delete":
        theList.delete(inp[i+1])
    elif command == "print":
        theList.print_list()