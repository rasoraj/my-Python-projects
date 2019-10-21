import random
print("Welcome!! This is Hangman, without hanging anyone :)")
print("You have 6 chances/lives in which you have to guess the movie name else GAME OVER!")
print("Here is the name with only vowels viewable")
c_str = random.choice(['joker','promethous','aladdin','hobbs and shaw','baby driver'])
str2 = ""
nos = 0                                                                    # no of characters already disclosed
sp = 0                                                                     # no of spaces in the name
used = [' ']                                                               # to get hold of characters already used

for i in range(0,len(c_str)):
    if  c_str[i] == 'e' or c_str[i] == 'i'  or c_str[i] == 'o' or c_str[i] == 'u' or c_str[i] == 'a':
        str2 = str2 + c_str[i] + ','
        nos = nos + 1                                            # placing the vowels as the prerequisites of the game

    elif c_str[i] == ' ':
        str2 = str2 + ' '
        sp = sp + 1
    else:
        str2 = str2 + '_,'


print(str2)

print("Your game starts now")
life = 6
lt = len(c_str) - (nos + sp)                           # modifying the length after all spaces and vowels are disclosed

while (life > 0) and lt > 0:
    let = input("enter letter")
    flg = 0

    for j in used:                                     # checking for used character
        if id(j) == id(let):
            print("character already used")
            flg = 1
                                                       # new character appended to the 'used' list
    if flg != 1:
        used.append(let)

    co = 0

    for i in range(0, len(c_str)):
        if c_str[i] == let:
            co += 1

    if(co > 0) and flg == 0:
        lt = lt - co
    else:
         life = life - 1
         print("You've lost one life :", life)

if(life > 0) and lt == 0:
    print("You've won the name is "+c_str)

else:
    print("You've lost the game. Better luck next time")














