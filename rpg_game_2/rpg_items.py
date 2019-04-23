"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time
import math

# DONE - make a SuperTonic item to the store, it will restore the hero back to 10 health points.
# DONE - add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
# DONE - add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
# DONE - come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.

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
        self.armor = 0
        self.evade = 0

    def evade_chance(self):
        if self.evade != 0:
            base = 10
            chance = 10
        else:
            chance = 0

        for i in range(math.trunc(self.evade/2)):
            base = base/2
            chance += base
        return round(chance,2)

    def receive_damage(self, points):
        randomChance = round(random.uniform(1,100),2)
        chance = self.evade_chance()
        armorBreak = 0
        if(randomChance >= chance):
            print('You evaded the attack! You took no damage')
        else:
            if self.armor > 0:
                if (self.armor - points) == 0:
                    self.armor -= points
                    print('Your armor breaks!')
                elif (self.armor - points) <= 0:
                    armorBreak = points-self.armor
                    self.armor = 0
                    print('Your armor absored %d damage' % (points-armorBreak))
                    self.health -= armorBreak
                    print("%s received %d damage." % (self.name, armorBreak))
                else:
                    self.armor -= points
                    print('Your armor absored %d damage' % points)
            else:
                self.health -= points
                print("%s received %d damage." % (self.name, points))

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
        self.power = 5
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

class SuperTonic(object):
    cost = 25
    name = 'super tonic'
    def apply(self,character):
        character.health += 10
        print("%s's health increased to %d." % (character.name, character.health))

class Evade(object):
    cost = 1
    name = 'evade'
    def apply(self,character):
        character.evade += 1
        print("%s's evade increased to %d." % (character.name, character.evade))

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
    items = [Tonic, Sword, SuperTonic, Evade]
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
enemies = [Goblin(), Wizard(),Shadow(),Medic()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")