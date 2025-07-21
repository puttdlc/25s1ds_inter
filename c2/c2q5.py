class funString():

    def __init__(self,string = ""):

        self.string = string

    def __str__(self):

        return(self.string)

    def size(self) :

        return len(self.string)

    def changeSize(self):

        finalString = ""
        for i in self.string:
            ordNum = ord(i)
            if ordNum >= 90:
                finalString += chr(ordNum-32)
            else:
                finalString += chr(ordNum+32)
        return finalString

    def reverse(self):

        return self.string[::-1]

    def deleteSame(self):
        
        finalString = ""
        appeared = []
        for i in self.string:
           if not i in appeared:
               finalString += i
               appeared.append(i)
        return finalString
               



str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())