# CONDITIONAL STATEMENTS

# 1) IF STATEMENTS

# marks=87
marks_if=97
if marks_if>90:
    print("you'll get a mobile")
print("Thanks")
print('\n')

# 2) IF ELSE STATEMENTS

marks_if_else=87
if marks_if_else>90:
    print("you'll get a mobile")
else:
    print('No Smartphone')
print("Thanks")
print('\n')

# 3) IF ELIF ELSE STATEMENTS

marks_if_elif_else=87
if marks_if_elif_else>90:
    print("you'll get a mobile")
elif marks_if_elif_else>80:
    print('Party')
else:
    print('Nothing')
print("Thanks")
print('\n')

# 4) NESTED STATEMENT

marks_if_nested=87
if marks_if_nested>80:
    print("you'll get a mobile")
    if marks_if_nested>85:
        print("you'll get a free trip")
else:
    print('Nothing')
print("Thanks")
print("\n")

# 5) SHORT HAND IF STATEMENT

marks_shortHand=87
if marks_shortHand>=85: print("Get a Trip Boy")
print("\n")

# 6) SHORT HAND IF ELSE STATEMENT

marks_shortHand=87
print("Get a Trip Boy") if marks_shortHand>=90 else print("Nothing")
print("\n")
