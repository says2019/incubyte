
"""
String Calculator

Create a simple String calculator with a method signature:

The method can take up to two numbers, separated by commas, and will return their sum.

Allow the Add method to handle an unknown amount of numbers

Allow the Add method to handle new lines between numbers (instead of commas).

Allow the Add method to handle different delimiters
"""

class StringCal:
    #Constructor create the instance variable
    def __init__(self,string):
        self.string = string
    # method can take up string, new lines between numbers, separated by commas, and will return their sum
    def add(self):
        separate = self.string.replace("\\n","-")
        separate = separate.replace("//", "")
        separate = separate.replace(";", "")
        separate = separate.split(",")
        sum_total = 0
        for i in separate:
            i = i.split("-")[0]
            sum_total = sum_total + int(i)
        return sum_total

#Enter the input
input = input("Enter comma separated numbers: ")

#Create the object
num = StringCal(input)

print(num.add())




"""
    EXPECTED OUTPUT:
    ----------------
    Input : Enter comma separated numbers: 1,2,3,4,5,6
    Output : 21
    Input : Enter comma separated numbers: 1\n,2,3\n,122\n,8
    Output : 136
    Input : Enter comma separated numbers: 1//\n2;,2//\n3;,3
    Output : 6
"""
