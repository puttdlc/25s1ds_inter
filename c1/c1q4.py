def odd_list(al):
    odds = []
    for i in al:
        if i % 2 == 1:
            odds.append(i)
    return odds


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)