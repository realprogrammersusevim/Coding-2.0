# This is meant to be a joke
first_num = input("Please enter the first number you would like to multiply: ")
second_num = input("Please enter the second number you would like to multiply: ")
product = int(first_num) * int(second_num)
for i in range(0, product):
    if i == product - 1:
        print("1", end="\n")
    else:
        print("1 +", end=" ")
