# 1) WAP to find the sum of all even no's upto 50

'''
sum=0
for i in range(1, 51):
    if i%2==0:
        sum+=i
print("The sum of all even no's upto 50 is",sum)
'''

# 2) WAP to write first 20 no's and their squared numbers

'''
for i in range(1,21):
    print("The number is", i, "and the square of", i, "is", i*i)
print()
'''

# 3) WAP to find the sum of first 10 odd numbers using while loop

'''
sum=0
n=0
while n<=20:
    if n%2==1:
        sum+=n
    n+=1
print("The sum of first 10 odd numbers is "sum)
print()
'''

# 4) WAP to check if a no is divisible by 8 & 12 upto 100 numbers

'''
for i in range(1, 101):
    if(i%8==0 and i%12==0):
    # if (i % 8 == 0 or i % 12 == 0):
            print(i)
    else:
        continue
print()
'''

# 5) WAP to create a billing system at supermarket
while True:
    name=input("Enter your Name: ")
    total = 0
    while True:
        quantity=int(input("Enter the quantity: "))
        amount=int(input("Enter the amount: "))
        total+=quantity*amount
        repeat=input("Do you wish to continue for items? ")
        if repeat.lower() == 'no':
            break
    print("-"*50)
    print("Your Bill is ")
    print("Name:", name)
    print("Amount to be paid is:", total)
    print("************ HAPPY SHOPPING!! THANK YOU ******************")
    print("-"*50)
    repeat1 = input("Do you want to repeat whole process again? ")
    if repeat1.lower() == 'no':
        break
print()