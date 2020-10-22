from random import randint
import statBlock

class CharSheet:
    def __init__(self):
        self.id = randint(000, 999)
        self.name = None
        self.role = None
        self.level = 0
        self.race = None
        self.background = None
        self.alignment = None

        self.stat_block = None
        self.modifiers = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "wisdom": 0,
            "intellect": 0,
            "charisma": 0,
        }
        self.passive_per = 0
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

    # Mutators
    # =========================================================

    def set_(self, input):
        self. = input



