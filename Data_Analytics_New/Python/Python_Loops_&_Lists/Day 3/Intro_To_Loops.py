# LOOPS

# 1) FOR LOOPS

'''
for i in range(1,6):
    print(i)

print("\n")
'''

'''
for i in range(1,6,2):
    print(i)

print("\n")
'''

'''
n=int(input("Enter No. Here: "))
for i in range(0,10):
    print(n," X ", i+1, " = ", 2*(i+1))

print("\n")

for i in range(1,11):
    print(n," X ", i, " = ", 7*i)

print("\n")
'''

# 2) WHILE LOOPS

'''
n=0
while n<=5:
    print(n)
    n+=1
print("\n")
'''

'''
n=int(input("Enter N: "))
i=1
while i<=10:
    print(n,"X", i, "=", n*i)
    i+=1
print("\n")
'''

# 3) WHILE TRUE LOOPS

'''
while True:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    print(num1+num2)
    repeat=input("Do you want to repeat program: ")
    if repeat=='no':
        break
'''

# 4) NESTED LOOPS

for i in range(1,4):
    for j in range(1,11):
        print(j, end="")
    print()

