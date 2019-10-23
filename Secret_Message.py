p_text = input("Enter some text : ")
i = 0
s_text = ""
print()
key = input("Enter any key between 1-26")

while i < len(p_text):
    if ord(p_text[i]) >= 65 and ord(p_text[i]) <= 90:
        tmp = ord(p_text[i]) + int(key)
        if tmp > 90:
            tmp = (tmp - 90) + 64
        s_text = s_text + chr(tmp)

    elif ord(p_text[i]) >= 97 and ord(p_text[i]) <= 122:
        tmp = ord(p_text[i]) + int(key)
        if tmp > 122:
            tmp = (tmp - 122) + 96
        s_text = s_text + chr(tmp)

    else:
        s_text = s_text + p_text[i]

    i = i + 1


print("The encrypted text :"+s_text)





