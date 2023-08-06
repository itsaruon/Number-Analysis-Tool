#Taking input from user
firstNumber = int(input("Enter an odd number "))
secondNumber = int(input("Enter another number "))


#Function that prints all numbers
def printAllNumbers (firstNumber,secondNumber):
    #Loop
    for x in range(firstNumber,1 + secondNumber):
        print(x , end = " ")

#Function that prints all odd numbers
def printOddNumbers (firstNumber, secondNumber):
    #Loop
    for x in range(firstNumber, secondNumber,2):
        print(x, end = " ")


#Function that returns the sum of all even numbers
def printSumOfEven (firstNumber, secondNumber):
    #Loop
    total = 0
    for x in range(firstNumber, secondNumber):
        if(x%2 == 0):
            secondNumber = x + secondNumber

    print (secondNumber)


#Function that returns the sum of the square of the odd numbers
def printSumOfSquare (firstNumber, secondNumber):
    #Loop
    sumValue = 0
    for x in range(firstNumber, 1+secondNumber):
        if x%2 != 0:
            sumValue += x**2
    print(float (sumValue))


print ("\nPrint All Numbers: ")
printAllNumbers (firstNumber, secondNumber)
print("\nPrint Odd Numbers: ")
printOddNumbers (firstNumber, secondNumber)
print ("\nPrint sum of the even numbers: ")
printSumOfEven (firstNumber, secondNumber)
print ("\nPrint sum of the square of the odd numbers: ")
printSumOfSquare (firstNumber, secondNumber)


 


