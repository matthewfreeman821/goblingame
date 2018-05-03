class Characters(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to you." % (self.name, self.power))
        return (enemy.health)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
        