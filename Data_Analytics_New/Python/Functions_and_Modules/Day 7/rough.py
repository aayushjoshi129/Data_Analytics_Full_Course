for i in range(0,5):
    for j in range(0,5):
        if(j==0 or i==4):
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()

print()

for i in range(0,5):
    for j in range(0,5):
        if((j==0 or j==4) or i==j):
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()