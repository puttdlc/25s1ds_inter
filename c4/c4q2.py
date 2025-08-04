class queue:
    def __init__(self, value=None):
        self.queue = value if value is not None else []
    def get_queue(self):
        return self.queue.copy()
    def dequeue(self):
        if self.queue:
            self.queue = self.queue[1:]
    def get_next(self):
        return self.queue[0] if self.queue else None
    def enqueue(self, value):
        self.queue.append(value)
    def isEmpty(self):
        return len(self.queue) == 0
    def getCount(self):
        return len(self.queue)

inp = input("Enter people : ")
main = queue(list(inp))
c1 = queue()
c2 = queue()

c1_timer = 0
c2_timer = 0
minute = 0

while not main.isEmpty():
    minute += 1

    if c1_timer == 0 and not c1.isEmpty():
        c1.dequeue()
        c1_timer = 3 if not c1.isEmpty() else 0

    if c2_timer == 0 and not c2.isEmpty():
        c2.dequeue()
        c2_timer = 2 if not c2.isEmpty() else 0

    if not main.isEmpty():
        person = main.get_next()
        if c1.getCount() < 5:
            main.dequeue()
            c1.enqueue(person)
            if c1.getCount() == 1:
                c1_timer = 3
        elif c2.getCount() < 5:
            main.dequeue()
            c2.enqueue(person)
            if c2.getCount() == 1:
                c2_timer = 2

    if c1_timer > 0:
        c1_timer -= 1
    if c2_timer > 0:
        c2_timer -= 1

    print(minute, main.get_queue(), c1.get_queue(), c2.get_queue())