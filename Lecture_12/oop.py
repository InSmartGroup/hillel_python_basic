import random
from oop_module import human_names, close_combat_weapons, armor_list, long_range_weapons


class Warrior:

    def __init__(self):
        self.name = random.choice(human_names)
        self.health = random.randint(80, 100)
        self.weapon = random.choice(close_combat_weapons)
        self.attack_power = random.randint(10, 50)
        self.armor = random.choice(armor_list)
        self.armor_class = random.randint(5, 10)


class Archer:

    def __init__(self):
        self.name = random.choice(human_names)
        self.health = random.randint(50, 80)
        self.weapon = random.choice(long_range_weapons)
        self.attack_power = random.randint(20, 60)
        self.armor = random.choice(armor_list)
        self.armor_class = random.randint(1, 5)


class Defender:

    def __init__(self):
        self.name = random.choice(human_names)
        self.health = 100
        self.weapon = random.choice(close_combat_weapons)
        self.attack_power = 50
        self.armor = random.choice(armor_list)
        self.armor_class = 10
