class queue:
    def __init__(self, value=[]):
        self.queue = value
    def dequeue(self):
        self.queue = self.queue[1::]
    def enqueue(self,value):
        self.queue.append(value)
    def isEmpty(self):
        return len(self.queue) == 0
    def getCount(self):
        return len(self.queue)
    
inp = input("Enter Input : ").split(",")

numbers = queue()

for batch in inp:
    if len(batch) > 1:
        instruction, value = batch.split()
        if instruction == "E":
            print(f"Add {value} index is {numbers.getCount()}")
            numbers.enqueue(value)
    elif batch[0] == "D":
        if numbers.isEmpty():
            print("-1")
        else:
            print(f"Pop {numbers.queue[0]} size in queue is {numbers.getCount()-1}")
            numbers.dequeue()

result = f"Number in Queue is :  {numbers.queue}" if numbers.getCount() > 0 else "Empty"
print(result)


