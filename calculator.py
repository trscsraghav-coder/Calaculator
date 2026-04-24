num_1= float(input("enter the first number: "))
op= input("enter operator +,-,*,/: ")
num_2= float(input("enter the second number: "))
if op== "+":
    print(num_1+num_2)
elif op== "-":
    print(num_1-num_2)
elif op== "*":
    print(num_1*num_2)
elif op== "/" and num_2!=0:
    print(num_1/num_2)
elif op== "/" and num_2==0:
    print("division by zero is not possible")
else: print("invalid operator")