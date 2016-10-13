c = input("Enter a three digit equation such as 3+5: ")
num1 = int(c[0])
op = c[1]
num2 = int(c[2])
if op == "+":
    num3 = num1 + num2
    print("The result is {}.".format(num3))
elif op == "-":
    num3 = num1 - num2
    print("The result is {}.".format(num3))
elif op == "*":
    num3 = num1 * num2
    print("The result is {}.".format(num3))
elif op == "/":
    num3 = num1 / num2
    print("The result is {}.".format(num3))
elif op == "%":
    num3 = num1 % num2
    print("The result is {}.".format(num3))