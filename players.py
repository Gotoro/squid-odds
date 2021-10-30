from random import randint
from os import system
from time import sleep

# squid game
# final game odds if all players played fair (ie, only 1 person can die per jump)
players_in_end = 0
games_count = 0
winning_percentage = {}
try:
    while True:
        players = 16
        glass = 18
        # if one player jumps and doesn't break the glass, then we remove that glass, as the path is known
        # if the player jumps and dies, we remove both the player and that glass
        while players > 0 or glass > 0:
          
            if players <= 0 or glass <= 0:
                break
                
            if randint(0, 1):
                glass -= 1
            else:
                glass -= 1
                players -= 1
        
        players_in_end += players
        games_count += 1
        
        if players not in winning_percentage:
            winning_percentage[players] = 0
            winning_percentage[players] += 1
        else:
            winning_percentage[players] += 1


        print(f"Total games played: {games_count}")
        print(f"Current average players at the end: {players_in_end // games_count}")
        system("cls")

except KeyboardInterrupt:
  
    print(f"Total games played: {games_count}")
    print(f"Current average players at the end: {players_in_end // games_count}")
    
    # sort dictionary
    winning_percentage = {x:winning_percentage[x] for x in sorted(winning_percentage)} 
    
    for x in winning_percentage:
        print(f"{x} has {(winning_percentage[x] / sum(winning_percentage.values()))*100:.2f}% chance of being in the end")
    exit()
