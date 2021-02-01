# Create function
# def sayHello(name="Ethan Hunt"):
#     print(f"Hello {name}")


# sayHello()

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total


num = getSum(10, 30)
print(num)

# Lambda Function

getSum = lambda num1, num2: num1+num2
print(getSum(10, 3))
