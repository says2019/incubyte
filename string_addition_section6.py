
"""
String Calculator

Create a simple String calculator with a method signature:

The method can take up to two numbers, separated by commas, and will return their sum.

Allow the Add method to handle an unknown amount of numbers

Allow the Add method to handle new lines between numbers (instead of commas).

Allow the Add method to handle different delimiters

Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed.
if there are multiple negatives, show all of them in the exception message.

Numbers bigger than 1000 should be ignored, so adding 2 +
"""

class StringCal:
    #Constructor create the instance variable
    def __init__(self,string):
        self.string = string
    # method can take up string, new lines between numbers, separated by commas, and will return their sum and negative number will throw an exceptions
    def add(self):
        negative_value = []
        separate = self.string.replace("\\n","--")
        separate = separate.replace("//", "")
        separate = separate.replace(";", "")
        separate = separate.split(",")
        sum_total = 0
        for i in separate:
            i = i.split("--")[0]

            if int(i) <= 0:
                negative_value.append(int(i))
            else :
                #Numbers bigger than 1000 should be ignored, so adding 2 +
                if int(i) >1000 :
                    sum_total = sum_total + 2
                else:
                    sum_total = sum_total + int(i)
        if len(negative_value) > 0:
            if len(negative_value) == 1:
                sum_total = "negatives not allowed"
            else:
                sum_total = "there are multiple negatives {}".format(negative_value)
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
    Input : Enter comma separated numbers: -1,2,3,4
    Output : negatives not allowed
    Input : Enter comma separated numbers: -1,-2,3,-4,-9//\n34;,10\n,4
    Output : there are multiple negatives [-1, -2, -4, -9]
    Input : Enter comma separated numbers: 1000,2,3,20000
    Output: 1007

"""
