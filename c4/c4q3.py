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

inp = input("input : ").split(',')

numbers = queue()
counter = 0
error_dequeue = 0
error_input = 0

for step in inp:
    print(f"Step : {step}")
    if step[0] == "D":
        for i in range(int(step[1])):
            if numbers.getCount() < 1:
                error_dequeue += 1
            else:
                numbers.dequeue()
        print(f"Dequeue : {numbers.get_queue()}")
    elif step[0] == "E":
        for i in range(int(step[1:])):
            numbers.enqueue(f"*{counter}")
            counter += 1
        print(f"Enqueue : {numbers.get_queue()}")
    else:
        error_input += 1
        print(numbers.get_queue())
    print(f"Error Dequeue : {error_dequeue}")
    print(f"Error input : {error_input}")
    print("--------------------")