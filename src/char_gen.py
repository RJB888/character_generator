"""Make a character generator."""

import random


class Character(object):
    """Define the char object."""

    def __init__(self, stgth=_stat_randomizer,
                 dex=_stat_randomizer,
                 con=_stat_randomizer,
                 wis=_stat_randomizer,
                 intel=_stat_randomizer,
                 cha=_stat_randomizer,
                 class_type=(random.randint(1, 4)),
                 race=random.randint(1, 4)):
        char_str = stgth
        char_dex = dex
        char_con = con
        char_wis = wis
        char_int = intel
        char_cha = cha
        char_race = self._race_gen(race)
        char_class = self._class_gen(class_type)
        char_hp = self._hp_calc()
        char_equipment = []

    def _stat_randomizer(self):
        return random(4, 22) -2

    def _race_gen(self, num):
        if num == 1:
            return "Human"
        elif num == 2:
            self.char_dex += 2
            self.char_int += 2
            self.char_con -= 2
            self.char_str -= 2
            return "Elf"
        elif num == 3:
            self.char_str += 2
            self.char_dex -= 2
            self.char_cha -= 2
            self.char_con += 2
            return "Dwarf"
        elif num == 4:
            self.char_cha += 2
            self.char_str -= 1
            self.char_wis -= 1
            self.char_con -= 1
            self.char_dex += 2
            return "Halfling"

    def _class_gen(self, num):
        if num == 1:
            return "Fighter"
        elif num == 2:
            return "Rogue"
        elif num == 3:
            return "Wizard"
        elif num == 4:
            return "Cleric"

    def _hp_calc(self):
        if self.char_class == "Fighter":
            self.char_hp = 10 + 
            if self.char_con >= 10:
                self.char_hp += (self.char_con - 10) / 2
        elif self.char_class == "Rogue":
            self.char_hp = 8 + 
            if self.char_con >= 10:
                self.char_hp += (self.char_con - 10) / 2
        elif self.char_class == "Wizard":
            self.char_hp = 6 + 
            if self.char_con >= 10:
                self.char_hp += (self.char_con - 10) / 2
        else:
            self.char_hp = 8 + 
            if self.char_con >= 10:
                self.char_hp += (self.char_con - 10) / 2

    def show_char(self):
        pass

    def _starting_equipment(self):
        if self.char_class == "Fighter":
            self.char_equipment = ["long sword", "plate armor"]
        elif self.char_class == "Rogue":
            self.char_equipment = ["dagger", "leather armor"]
        elif self.char_class == "Wizard":
            self.char_equipment = ["staff", "robes"]
        else:
            self.char_equipment = ["mace", "chain armor"]

    """
    Stuff it should have::

    Str
    Dex
    Con
    Wis
    Int
    Cha

    Class
    Race

    Weapon
    Armor

    AC
    HP

    

    """