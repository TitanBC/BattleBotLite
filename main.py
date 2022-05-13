import combat
import random
import stats

game = True
combat = False
#print(stats.weapon_list[str(random.randint(1,3))])

while game:
  player_health = int(input("Enter player hit points: \n"))
  player_weapon = str(input("Choose a weapon! \n 1: Sword \n 2: Spear \n 3: Greatsword \n"))
  player_armor = str(input("Select your armor! \n 1:Leather \n 2: Chainmail \n 3: Plate Armor \n"))
  print(f"You have {player_health} hit points, you are holding a {stats.weapon_list[player_weapon]}, and you are wearing {stats.armor_list[player_armor]}!")
  
  monster_type = str(random.randint(1,3)) 
  monster_weapon = str(random.randint(1,3))
  monster_armor = str(random.randint(1,3))

  print(f"You will fight a {stats.monster_list[monster_type]}, holding a {stats.weapon_list[monster_weapon]}, wearing {stats.armor_list[monster_armor]}!!")

  combat_condit = input(f"Would you like to engage in combat??!?: Y/N \n")
  if combat_condit == "Y" or combat_condit == 'y':
    combat = True
  while combat = True:
    monster_roll = random.randint(1,20)
    player_roll = random.randint(1,20)
