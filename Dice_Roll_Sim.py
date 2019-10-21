import random

while True:
    v = input("Roll")
    no = random.choice([1,2,3,4,5,6])
    print(no)
    ch = input("To continue press 'c' else 'e' to exit")
    if ch == 'e':
        break




