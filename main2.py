import combat
import random
import stats
import monsters
import playergen
turn_toggle = 1


# health_input = int(input("How much HP? "))
# weapon_input = input("Select weapon: \n (1) sword & shield \n (2) Spear \n (3) Greatsword \n")
# weapon_input = stats.weapon_list[weapon_input]
# armor_input = input("Select armor: \n (1) leather armor \n (2) chain mail  \n  (3) plate armor \n")
# armor_input = stats.armor_list[armor_input]
# speed_input = 0

player_one = playergen.Player()
player_two = playergen.Player()

print(f"Player one health is: {player_one.health} \n")
print(f"Player one weapon damage is: {player_one.wep_dmg} \n")
print(f"Player one armor bonus is: {player_one.armor_bonus} \n")

print(f"Player two health is: {player_two.health} \n")
print(f"Player two weapon damage is: {player_two.wep_dmg} \n")
print(f"Player two armor bonus is: {player_two.armor_bonus} \n")

print("SIMULATE ATTACK \n SIMULATE ATTACK \n SIMULATE ATTACK \n")

player_one.health -= combat.roll_dmg(player_two.wep_dmg)
print(player_one.health)

print("NEW ATTACK")

player_one.health -= combat.roll_dmg(player_two.wep_dmg)
print(player_one.health)

print("NEW ATTACK")

player_one.health -= combat.roll_dmg(player_two.wep_dmg)
print(player_one.health)


# player_two = playergen.Player(health_input, weapon_input, armor_input, speed_input)

# player_one.health -= combat.roll_dmg(player_one.wep_dmg)
# player_one.health -= combat.roll_dmg(player_one.wep_dmg)
# player_one.health -= combat.roll_dmg(player_one.wep_dmg)
# print(player_one.health)

#player_one_dmg = stats.weapon_list['greatsword']['damage']
# player_one_def = stats.

# player_two_dmg = stats. 
# player_two_def = stats.