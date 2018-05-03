from characters1 import Characters
from hero import Hero
from goblin import Goblin


def main():
    hero = Hero('Matt', 10, 5)
    goblin = Goblin('Goblin', 6, 2)
    while goblin.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight %s" % (goblin.name))
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks enemy
            hero.attack(goblin)
            print("You do %d damage to the %s." % (hero.power, goblin.name))
            if goblin.health <= 0:
                 print("The %s is dead." % (goblin.name))
        elif user_input == "2":
            goblin.attack(hero)
            hero.print_status()
        elif user_input == "3":
            print("Goodbye.")
        else:
            print("Invalid input %r" % user_input)
        if hero.health <= 0:
                print("You are dead.")
main()