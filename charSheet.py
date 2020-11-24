from random import randint
from statBlock import StatBlock
import operator


class CharSheet:
    def __init__(self):
        self.id = randint(000, 999)
        self.name = None
        self.role = None
        self.level = 1
        self.race = None
        self.background = None
        self.alignment = None

        self.stat_block = StatBlock()
        self.modifiers = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "wisdom": 0,
            "intellect": 0,
            "charisma": 0,
        }
        self.passive_per = 10
        self.ds_success = 0
        self.ds_fail = 0

        self.personality = None
        self.ideals = None
        self.bonds = None
        self.flaws = None

        self.held_weapon = None
        self.worn_armor = None

        self.feats_traits = []
        self.prof_langs = []
        self.inventory = []
        self.spells = []

    # Accessors
    # =========================================================
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_role(self):
        return self.role

    def get_level(self):
        return self.level

    def get_race(self):
        return self.race

    def get_background(self):
        return self.background

    def get_alignment(self):
        return self.alignment

    def get_base_stat(self, stat):
        return self.stat_block.get_stat(stat)

    def get_modifier(self, modifier):
        return self.modifiers.get(modifier, default = None)

    def get_passive_per(self):
        return self.modifiers.get("wisdom") + 10

    def get_ds_success(self):
        return self.ds_success

    def get_ds_fail(self):
        return self.ds_fail

    def get_personality(self):
        return self.personality

    def get_ideals(self):
        return self.ideals

    def get_bonds(self):
        return self.bonds

    def get_flaws(self):
        return self.flaws

    def get_weapon(self):
        return self.held_weapon

    def get_armor(self):
        return self.worn_armor

    def get_feat(self, item):
        if type(item) is not int:
            if item in map(operator.itemgetter(0), self.feats_traits):
                x = [y[0] for y in self.feats_traits].index(item)
                return list(map(operator.itemgetter(1), self.feats_traits))[x]
        else:
            return self.feats_traits[item][0]

    def get_feat_size(self):
        return len(self.feats_traits)

    def get_feats(self):
        return self.feats_traits

    def get_prof(self, prof):
        for i in self.prof_langs:
            if i == prof:
                return self.prof_langs[i]
            else:
                return None

    def get_item(self, item):
        for i in self.inventory:
            if i == item:
                return self.inventory[i]
            else:
                return None

    def get_spell(self, spell):
        for i in self.spells:
            if i == spell:
                return self.spells[i]
            else:
                return None

    # Mutators
    # =========================================================

    def set_name(self, string):
        self.name = string

    def set_id(self, num):
        self.id = num

    def set_role(self, string):
        self.role = string

    def level_up(self):
        if self.level < 20:
            self.level += 1

    def set_level(self, num):
        if 0 < num <= 20:
            self.level = num
            return True
        return False

    def set_race(self, string):
        self.race = string

    def set_background(self, string):
        self.background = string

    def set_alignment(self, string):
        self.alignment = string

    def set_base_stat(self, stat, num, face=None):
        self.stat_block.modify_stat(stat, num, face)

    def set_modifier(self, modifier, value):
        self.modifiers[modifier] = value

    def ds_success(self):
        self.ds_success += 1

    def ds_fail(self):
        self.ds_fail += 1

    def set_personality(self, string):
        self.personality = string

    def set_ideals(self, string):
        self.ideals = string

    def set_bonds(self, string):
        self.bonds = string

    def set_flaws(self, string):
        self.flaws = string

    def swap_weapon(self, swap):
        temp = self.get_item(swap)
        if temp is not None:
            self.inventory.append(self.held_weapon)
            self.held_weapon = temp

    def swap_armor(self, swap):
        temp = self.get_item(swap)
        if temp is not None:
            self.inventory.append(self.worn_armor)
            self.worn_armor = temp

    def add_feat(self, name, desc):
        self.feats_traits.append((name, desc))

    def add_prof(self, name, desc):
        self.prof_langs.append((name, desc))

    def add_to_inv(self, item):
        self.inventory.append(item)

    def add_spell(self, name, desc):
        self.spells.append((name, desc))



