print("Introduction to programming, Lab № 2")
print("Didenko Oleksii IKM-221д")

TEMPLATE = "Enter {}"
x = int(input(TEMPLATE.format('x: ')))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

a = (((z-23.1)*(2**x+2.2))/(y-21.1)-3.2)
print("Result is: ", a)