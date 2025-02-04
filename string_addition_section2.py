"""
String Calculator

Create a simple String calculator with a method signature:

The method can take up to two numbers, separated by commas, and will return their sum.

Allow the Add method to handle an unknown amount of numbers
"""
class StringCal:
    #Constructor create the instance variable
    def __init__(self,string):
        self.string = string
    # method can take up string, separated by commas, and will return their sum
    def add(self):
        separate = self.string.split(",")
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
    Input : Enter comma separated numbers: 1,2,3,4,5
    Output : 15

"""
