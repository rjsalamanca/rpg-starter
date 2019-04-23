# RPG Starter Files

Starter files needed for Hero Game RPG exercises

## RPG Game 1

**Solutions for RPG Game 1 stored in: person_oop_exercise.py**

Take version 1 of the RPG game and rewrite it using objects.

### Step 1

Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health and goblin_power all through out the app.

### Step 2
Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)

### Step 3
Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero).

### Step 4

Refactor the while condition:

    while goblin.health > 0 and hero.health > 0:

to

    while goblin.alive() and hero.alive():

The health checks should be moved to within the alive methods of Hero and Goblin respectively.

### Step 5
Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the same for the goblin.

### Step 6

Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called Character and make both Hero and Goblin inherit from it.

### Step 7

The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and Goblin - now they can simply inherit it from Character.

### Step 7: Bonus Challenge

The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to move them into the Character class as well? Give it a try.

### Step 8: Bonus Challenge 2

Create a zombie character that cannot die and have it fight the hero instead of the goblin.