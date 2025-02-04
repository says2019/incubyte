"""
String Calculator

Create a simple String calculator with a method signature:

The method can take up to two numbers, separated by commas, and will return their sum.

Allow the Add method to handle an unknown amount of numbers

Allow the Add method to handle new lines between numbers (instead of commas).
"""
class StringCal:
    #Constructor create the instance variable
    def __init__(self,string):
        self.string = string
    # method can take up string, new lines between numbers, separated by commas, and will return their sum
    def add(self):
        separate = self.string.replace("\\n","")
        separate = separate.split(",")
        sum_total = 0
        for i in separate:
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
    Input : Enter comma separated numbers: 1\n,2\n,3\n,4
    Output : 10
"""
