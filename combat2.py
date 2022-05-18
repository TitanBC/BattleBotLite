import combat
import random
import stats
import monsters
import playergen

def roll_hit(check):
  roll = random.randint(1,20)
  if roll >= check:
    result = True
  elif roll < check:
    result = False
  return result


def roll_dmg(wep_dmg):
  roll_dmg = random.randint(1,wep_dmg)
  return roll_dmg

def attack(atk_dmg, def_armor):
  hit_condit = roll_hit(def_armor)
  if hit_condit == true:
    damage = roll_dmg(atk_dmg)
    



