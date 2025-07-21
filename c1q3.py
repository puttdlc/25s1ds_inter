print(" *** Summation of each digit ***")
inp = input("Enter a positive number : ")

summation = 0
for i in range(0,len(inp)):
    summation += int(inp[i])

print(f"Summation of each digit =  {summation}")
