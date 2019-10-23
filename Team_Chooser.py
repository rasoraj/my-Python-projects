import random

players = ['riabh','rasan','dinaka','hamidh','elanni','aspha']
team = [ 'Aligators','Panthers','Gorillas','Pythons','Wasps']

random.shuffle(players)
random.shuffle(team)

i = 0
j = int(len(team)/2) + 1

print(team[0]+" : ", end="")
while i < (len(team)/2):
    print(players[i]+", ", end="")
    i= i+1

print()

print(team[1]+" : ", end="")
while j < len(players):
    print(players[j]+", ", end="")
    j = j+1

print()