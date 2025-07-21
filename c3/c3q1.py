inp = input("Enter Input : ").split(',')

stack = []

for chunk in inp:
    value = None
    command = chunk[0]
    if " " in chunk:
        value = chunk.split()[1]
    if command == "A":
        stack.append(value)
        print(f"Add = {value} and Size = {len(stack)}")
    if command == "P":
        if len(stack) > 0:
            print(f"Pop = {stack[-1]} and Index = {len(stack)-1}")
            stack.pop()
        else:
            print("-1")
print("Value in Stack = ",end='')
if len(stack) > 0:
    valuesString = ""
    for value in stack:
        valuesString += value + " "
    print(valuesString[:-1])
else:
    print("Empty")
