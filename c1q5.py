inp = input("Enter All Bid : ").split()

def getSorted(arr):
    numberForm = []
    for i in inp:
        numberForm.append(int(i))
    numberForm.sort()
    numberForm.reverse()
    return numberForm

if len(inp) <= 1:
    print("not enough bidder")
else:
    result = getSorted(inp)
    if result[0] == result[1]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {result[0]} need to pay {result[1]}")