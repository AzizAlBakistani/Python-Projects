print("This is a simple Calculator so kindly use only +, _, * and/")
a = int(input("Enter the first Variable ="))
b = int(input("Enger the Second Variable ="))
opr = input("Operator")

if opr == "+":
    print("your Answer is", a+b)

elif opr == "-":
    print("Your Answer is:", a-b)

elif opr == "*":
    print("Your Answer is:,", a*b)

elif opr == "/":
    print("Your Answer is:", a/b)

else:
    print("Kindly use a valid operator")
