from character import Character
from colorama import Fore



player1 = Character(name='Vasya', health=70, damage=10, defence=0,
                    color=Fore.LIGHTRED_EX)
print(player1)

player2 = Character(name='Petya', health=70, damage=10, defence=0,
                    color=Fore.LIGHTBLUE_EX)

print(player2)
player1.attack(player2)

print(player2)
player1.attack(player2)

print(player1)
player2.attack(player1)

print(player2)
player1.attack(player2)

print(player1)
player2.attack(player1)

print(player2)
player1.attack(player2)

print(player1)
player2.attack(player1)

print(player2)
player1.attack(player2)

print(player1)
player2.attack(player1)

print(player2)
player1.attack(player2)

print(player1)
player2.attack(player1)

print(player2)
player1.attack(player2)


print(player1)
print(player2)

if player2:
    player2 = health=0
    print('Vasua Победил')

if player1:
    player1 = health=0
    print('Petya Победил')