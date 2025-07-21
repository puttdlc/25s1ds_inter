print("* Stack Calculator *")
inp = input("Enter arguments : ").split()

class stack:
    def __init__(self, values):
        self.stack = values
    def push(self, value):
        self.stack.append(value)
        #print(f"pushed {value}")
    def pop(self):
        if len(numbers.stack) > 0:
            temp = self.stack[-1]
            #print(f"popped {temp}")
            self.stack.pop()
            return temp
        else:
            return 0

numbers = stack([])

validInstructions = ["+","-","*","/","DUP","POP","PSH"]

def Verified():
    for value in inp:
        if not value.isdigit() and not value in validInstructions:
            print(f"Invalid instruction: {value}")
            return False
    return True

if Verified():
    #print("BEGIN")
    #print(numbers.stack)
    #print(instructions.stack)
    mem = 0
    for instruction in inp:
        #print(f"\nmem: {mem} instruction: {instruction}\n")
        if instruction.isdigit():
            numbers.push(instruction)
        mem = int(numbers.stack[-1])
        if instruction in validInstructions:
            if instruction == "+":
                mem = int(numbers.pop()) + int(numbers.pop())
                numbers.push(mem)
            elif instruction == "-":
                mem = int(numbers.pop()) - int(numbers.pop())
                numbers.push(mem)
            elif instruction == "*":
                mem = int(numbers.pop()) * int(numbers.pop())
                numbers.push(mem)
            elif instruction == "/":
                mem = int(numbers.pop()) // int(numbers.pop())
                numbers.push(mem)
            elif instruction == "DUP":
                numbers.push(numbers.stack[-1])
            elif instruction == "POP":
                numbers.pop()
    mem = numbers.pop()
    print(mem)

#print(numbers.stack)
#print(instructions.stack)