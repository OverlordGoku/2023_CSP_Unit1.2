#Write a method called addSubtract()
#This method should take a parameter called operation
#When the method is called, ask the user for two numbers
#Do the operation of the parameter to the inputs
#the parameter to all numbers in the lists

def addSubtract(operation):
    num1 = [2, 5, 6, 98, 32, 123]
    num2 = [5, 67, 89, 34, 1, 4]


index=0
#For each loop - kiedes style
for val in num1:
    if operation == "add":
        print(num1[index]+num2[index])
    else:
        print(num1[index]-num2[index])
        index+=1
'''''''''
def addSubtract(operation):
    num1 = input("What is the first number?")
    num2 = int(input("What is the second number?"))
    If (operation=="add"):
    print(num1+num2)

    else:
        print(num1-num2)
        
    other option of loop:
    for index in range(num1.length()-1)
'''''
addSubtract("add")
addSubtract("subtract")
