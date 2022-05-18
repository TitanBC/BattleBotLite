import random

class Goblin:

  def __init__(self, health, initiative):
    self.health = health
    self.initiative = initiative
    
  
  def goblin_moves():

    def goblin_attack():
      damage = random.randint(1,10)
      print(f"The goblin attacks you for {damage} damage!")
      return damage

    def goblin_spell():
      spell_dmg = random.randint(6,12)
      print(f"The goblin casts a spell hitting you for {spell_dmg} damage!")
      return spell_dmg
    
    def goblin_taunt():
      taunt_select = random.randint(1,3)
      if taunt_select == 1:
        print("Yar I be a goblin")
      elif taunt_select == 2:
        print("Your mother is a hooker")
      elif taunt_select == 3:
        print("I don't have any goblin jokes")
      return 0
    
    move_select = random.randint(1,2)
    if move_select == 1:
      damage = goblin_attack()
      return damage
    if move_select == 2:
      damage = goblin_spell()
      return damage
    if move_select == 3:
      goblin_taunt()
      return goblin_taunt()
    
      
    






class giant:

  def __init__(self, health, initiative):
    self.health = health
    self.initiative = initiative

  def giant_moves():
    
    def giant_attack():
      damage = random.randint(10,15)
      return damage
  
    def giant_regen():
      regen = random.randint(1,4)
      return regen
  
    def giant_tired():
      print(f"The slow-moving giant takes a break!")
  
    move_select = random.randint(1,3)
    if move_select == 1:
      damage = giant_attack()
      return damage
    elif move_select == 2:
      regen = giant_regen()
      return regen
    elif move_select == 3:
      giant_tired()