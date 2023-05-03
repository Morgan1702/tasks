# Introduction to programming, Lab № 4
# Didenko Oleksii IKM-221д

print('Introduction to programming, Lab № 4')
print('Didenko Oleksii IKM-221д')

TEMPLATE = "Enter {}"
N = int(input("Enter N: "))
M = int(input("Enter M: "))
for i in range(N, M+1):
    if i%2 == 0 or i%3 == 0:
        print(i)