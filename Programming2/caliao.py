class Character:
    def __init__(self, name, health):
        self._name = name
        self._health = health

    def get_name(self):
        return self._name
    def get_health(self):
        return self._health
    def get_damage(self, damage):
        self._health -= damage
        print(f"{self._name} took {damage}! Health is now {self._health}.")
    def attack (self):
        print(f"{self._name} cast a basic attack!")

class Fighter(Character):
    def attack(self):
        print (f"{self._name} swings a sword!")

class Mage(Character):
    def attack(self):
        print (f"{self._name} cast a thunder!")

c = Character()
f = Fighter("Aragon", 100)
m = Mage("Gandalf", 80)

character = [f,m]
for c in character:
    c.attack()

f.get_damage(30)
m.get_damage(20)

print(f"{f.get_name()}'s Health {f.get_health()}")
print(f"{m.get_name()}'s Health {m.get_health()}")