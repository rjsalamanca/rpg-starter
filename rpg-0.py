"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character:
    def __init__(self,culture,health,power):
        self.culture = culture
        self.health = health
        self.power = power

    def attack(self,opponent): 
        if opponent.culture is 'Zombie':
            print('Zombies cannot die, the %s does %d damage, but the zombie is still alive!' % (self.culture,self.power))

        else:

            opponent.health = opponent.health - self.power
            print("The %s does %d damage to the %s." % (self.culture,self.power,opponent.culture))

        return opponent.health

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def status(self):
        print("The %s has %d health and %d power." % (self.culture,self.health, self.power))

class Hero(Character):
    def __init__(self,culture,health,power):
        Character.__init__(self,culture,health,power)
    
class Goblin(Character):
    def __init__(self,culture,health,power):
        Character.__init__(self,culture,health,power)

def main():
    hero = Hero('Hero',10,5)
    goblin = Goblin('Goblin',6,2)
    zombie = Character('Zombie',10,1)

    while zombie.alive() and hero.alive():
        hero.status()
        zombie.status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
            if zombie.alive() == False:
                print("The zombie is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if zombie.health > 0:
            # zombie attacks hero
            zombie.attack(hero)
            if hero.alive() == False:
                print("You are dead.")

main()