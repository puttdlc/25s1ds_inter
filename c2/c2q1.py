class translator:

    numeralValues = {
        "M" : 1000,
        "CM" : 900,
        "D" : 500,
        "CD" : 400,
        "C" : 100,
        "XC" : 90,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1,
    }

    def deciToRoman(self, num):
        currentSum = 0
        finalString = ""
        for symbol,value in self.numeralValues.items():
            while currentSum + value <= num:
                currentSum += value
                finalString += symbol
        return finalString

    def romanToDeci(self, roman):
        resultSum = 0
        workingString = roman
        offset = 0
        while offset < len(roman):
            for symbol, value in self.numeralValues.items():
                if workingString[offset:offset+len(symbol)] == symbol:
                    resultSum += value
                    offset += len(symbol)
                    break
        return resultSum

print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))