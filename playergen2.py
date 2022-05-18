import combat
import random
import stats
import monsters



class Player:
  
  def __init__(self):
    self.health = int(input("How much HP? "))

    weapon_input = input("Select weapon: \n (1) sword & shield \n (2) Spear \n (3) Greatsword \n") #select weapon from list
    weapon_name = stats.weapon_list[weapon_input] #convert selection input to dictionary key
    armor_input = input("Select armor: \n (1) leather armor \n (2) chain mail  \n  (3) plate armor \n") #select armor from list
    armor_name = stats.armor_list[armor_input] #convert input to dictionary key
    
    self.wep_dmg = stats.weapon_dict[weapon_name]['damage']
    self.armor_bonus = stats.armor_dict[armor_name]['armor bonus']
    self.speed_bonus = stats.armor_dict[armor_name]['speed bonus']
    self.armor_bonus += stats.weapon_dict[weapon_name]['armor bonus']  #this adds the armor bonus from weapon
    
  
  
  
  
    
class MonsterRandom:
  def __init__(self):
    monster_type = str(random.randint(1,3)) 
    monster_weapon = str(random.randint(1,3))
    monster_armor = str(random.randint(1,3))
    # self.armor_bonus = stats.weapon_list[weapon['armor bonus']] + stats.armor_list[armor['armor bonus']]
    # self.speed_bonus = stats.armor_list[armor['speed bonus']]

