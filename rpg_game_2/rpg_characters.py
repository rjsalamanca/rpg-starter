"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time

# DONE - make the hero generate double damage points during an attack with a probabilty of 20%
# DONE - make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
# DONE - make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
# DONE - come up with at least two other characters with their individual characteristics, and implement them.
# DONE - Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        
    def alive(self):
        if self.name == 'zombie':
            return True
        else:
            return self.health > 0

    def rewards(self,enemy):
        print('%s dropped %d coins' % (enemy.name.capitalize(),enemy.coins))
        self.coins += enemy.coins

    def attack(self, enemy):
        probabilty = random.randint(1,5)
        powerBonus = 0

        if self.name == 'hero':
            if probabilty == 1:
                powerBonus = self.power
                print('GOT A POWER BONUS')

        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power+powerBonus)
        time.sleep(1.5)

    def receive_damage(self, points):

        probabilty = random.randint(1,5)
        probability10Percent = random.randint(1,10)

        if self.name == 'medic':
            if probabilty == 1:
                points -= 2
                print('The medic was able to recuperate 2 health! The medic now has %d health.' % self.health)
        elif self.name =='shadow':
            if probability10Percent != 1:
                print('The shadow was able to dodge your attack. You\'ve done %d damage' % 0)
                points = 0
            else:
                print('You were able to hit the shadow!')

        self.health -= points
        print("%s received %d damage." % (self.name, points))

        if self.health <= 0:
            if self.name == 'zombie':
                print('Zombie is immortal!')
            else:
                print("%s is dead." % self.name)


    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 1
        self.power = 1
        self.coins = 100000

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2
        self.coins = 30

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 20
        self.power = 1
        self.coins = 2

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the %s" % enemy.name)
            hero.rewards(enemy)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)



hero = Hero()
enemies = [Medic(),Goblin(), Wizard(),Shadow()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")