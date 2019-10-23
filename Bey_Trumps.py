fl = open('cards','r')
beys = {}
for line in fl.read().splitlines():
    name, power, endurance, death_move = line.split(',')
    beys[name] = [power, endurance, death_move]

ch = input("Choose your bey-blade creature : ")

if ch in beys:
    print(beys[ch])
else:
    print("Sorry!! not found")

fl.close()