import random

ac = random.randint(100, 999)
print("Think of a 3 digit no")

while True:

    th = int(input("enter it and press Enter   :"))
    if (th == ac):
        print("Superb!!  guessed it right")
        break
    elif (th > ac):
        print("higher thoughts...often overshoots!")
    else:
        print("Make it higher!!!")
