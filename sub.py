# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))