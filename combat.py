import random

def roll_attack():
  roll = random.randint(1,20)
  return roll
def roll_damage(wep_damage):
  roll = random.randint(1,int(wep_damage))
  return roll

def int_roll(player_bonus, monster_bonus):
  player_roll = random.randint(1,20)
  monster_roll = random.randint(1,20)
  player_roll += player_bonus
  monster_roll += monster_bonus


