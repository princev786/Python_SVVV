password = input("Enter a passowrd :")
#Prince108@
hasUpper=False
hasDigit=False
hasSymbol=False
hasLen=len(password)>=8
for i in password:
    if i.isupper():
        hasUpper=True
    elif i.isdigit():
        hasDigit=True
    elif i.islower():
        hasLower = True
    else:
        hasSymbol = True

if hasSymbol and hasDigit and hasUpper and hasLen :
    print("Strong")
else:
    print("Weak")
