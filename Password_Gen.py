import random
storage = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+abcdefghijklmnopqrstuvwxyz"
no = int(input("Enter no. of Passwords you require : "))
le = int(input("Enter the length of your Password : "))

for i in range(no):
    str = ""
    for j in range(le):
        str = str + random.choice(storage)
    print(str)

