# Introduction to programming, Lab № 3
# Didenko Oleksii IKM-221д
import math
import math as m

print('Introduction to programming, Lab № 3')
print('Didenko Oleksii IKM-221д')

TEMPLATE = "Enter {}"
x = int(input(TEMPLATE.format('x: ')))
a: int = int(input("Enter a: "))

if x-4 <= 0 or 2*a-x == 0:
    raise Exception("The argument and base of the logarithm cannot be equal to zero and negative numbers or Exponent can not be 0")
else:
    result = (math.log2(x-4+math.exp(2*a-x)))
    print(f"Result: {result}")