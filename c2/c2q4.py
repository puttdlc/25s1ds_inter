inp = input("Enter Your List : ").split()
nums = [int(i) for i in inp]

length = (len(nums))

matching = []

if length > 2:
    for _ in range(length):
        for i in range(0,length):
            for x in range(1,length):
                for y in range(2,length):
                        arr1 = [nums[i],nums[x],nums[y]]
                        if sum(arr1) == 0:
                            sorted = arr1.copy()
                            sorted.sort()
                            if not sorted in matching:
                                matching.append(sorted)
    print(matching)
else:
    print("Array Input Length Must More Than 2")

