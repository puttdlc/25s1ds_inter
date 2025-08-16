class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return "->".join(result)
    def str_reverse(self):
        current = self.tail
        result = []
        while current:
            result.append(str(current.data))
            current = current.prev
        return "->".join(result)
    def isEmpty(self):
        return self.head is None
    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def insert(self, index, data):
        new_node = Node(data)
        if index < 0:
            return False
        if index == 0:
            if self.isEmpty():
                temp = new_node
                self.tail = temp
                self.head = temp
            else:
                old_head = self.head
                self.head = new_node
                new_node.next = old_head
                old_head.prev = new_node
            return True
        else:
            current = self.head
            i = 0
            while current and i < index:
                current = current.next
                i += 1
            if i < index:
                return False
            if not current:
                self.append(data)
                return True
            prev_node = current.prev # connect's inserted node's previous and next inbetween existing ones
            new_node.prev = prev_node
            new_node.next = current
            if prev_node: # connects previous's next to inserted node
                prev_node.next = new_node
            current.prev = new_node
            return True
    def remove(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                if current.prev:  # bypasses current's next
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:  # bypasses current's prev
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return index  # Return the removed node index
            current = current.next
            index += 1
        print("Not Found!")
        return None
inp = input("Enter Input : ").split(',')

theList = DoublyLinkedList()

for chunk in inp:
    if chunk[0] == " ":
        chunk = chunk[1:]
    command, data = chunk.split(' ')
    if command == "A": # Add 
        theList.append(data)
    elif command == "Ab": # Add Before
        theList.insert(0,data)
    elif command == "I": # Insert
        index, data = data.split(':')
        index = int(index)
        success = theList.insert(index, data)
        if success:
            print(f"index = {index} and data = {data}")
        else:
            print("Data cannot be added")
    elif command == "R": # Remove
        removedIndex = theList.remove(data)
        if removedIndex != None:
            print(f"removed : {data} from index : {removedIndex}")
    print(f"linked list : {theList}")
    print(f"reverse : {theList.str_reverse()}")

