def RANGE(*args):
    start = 0
    end = 0
    step = 1
    
    if len(args) == 1:
        start = 0
        end = args[0]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]

    sum = start
    final = "("
    while sum < end:
        final += str(float(round(sum,3)))
        if (sum + step) < end:
            final += ", "
        sum += step
    final += ")"
    return final

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))