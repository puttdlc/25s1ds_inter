class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class VIMSimulator:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursorIndex = 0
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return "->".join(result)
    def cursorLeft(self):
        if self.cursorIndex - 1 >= 0:
            self.cursorIndex -= 1
    def cursorRight(self):
        if self.cursorIndex < theList.getCount():
            self.cursorIndex += 1
    def isEmpty(self):
        return self.head is None
    def getCount(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count
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
    def remove_at_index(self, index):
        if index < 0 or index > self.getCount():
            return None
        currentIndex = 0
        current = self.head
        while current:
            if currentIndex == index:
                if current.prev:  # bypasses current's next
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:  # bypasses current's prev
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True  # success
            current = current.next
            currentIndex += 1
    def print_list_with_cursor(self):
        index = 0
        values = []
        current = self.head
        while index <= self.cursorIndex or current:
            if index == self.cursorIndex:
                values.append("|")
            else:
                values.append(current.data)
                current = current.next
            index += 1
        print(" ".join(values))
    
theList = VIMSimulator()

inp = input("Enter Input : ").split(',')

for chunk in inp:
    command = chunk[0]
    #print(command)
    if command == "L": # Cursor to Left
        theList.cursorLeft()
    if command == "R": # Cursor to Left
        theList.cursorRight()
    if command == "I": # Add 
        _, data = chunk.split(' ')
        theList.insert(theList.cursorIndex,data)
        #theList.cursorIndex = theList.getCount()
        theList.cursorRight()
    elif command == "B": # Backspace (Delete to Left)
        success = theList.remove_at_index(theList.cursorIndex-1)
        if success:
            theList.cursorLeft()
    elif command == "D": # Backspace (Delete to Left)
        success = theList.remove_at_index(theList.cursorIndex)
        if success:
            theList.cursorRight()
theList.print_list_with_cursor()