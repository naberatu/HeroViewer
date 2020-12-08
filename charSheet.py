from stat_block import StatBlock
import math
import pickle


class CharSheet:
    def __init__(self):
        # try:
        self.stats = pickle.load(open("hero_info.p", "rb"))
        # except:
        #     self.stats = StatBlock().get()
        #     pickle.dump(self.stats, open("hero_info.p", "wb"))

        self.modifier = {
            "strength": self.calc_modifier("strength"),
            "dexterity": self.calc_modifier("dexterity"),
            "constitution": self.calc_modifier("constitution"),
            "wisdom": self.calc_modifier("wisdom"),
            "intellect": self.calc_modifier("intellect"),
            "charisma": self.calc_modifier("charisma"),
        }
        self.ds_success = 0
        self.ds_fail = 0

        # self.personality = None
        # self.ideals = None
        # self.bonds = None
        # self.flaws = None

        # self.held_weapon = None
        # self.worn_armor = None

        self.feats_traits = pickle.load(open("feats_dict.p", "rb"))
        # self.prof_langs = {}
        # self.inventory = []
        # self.spells = {}

        # load_feats = {"Warrior": "Once per short rest, you can take a bonus action.",
        #               "Tamer": "Grants +2 Nature",
        #               "Alert": "+ Gain +5 Initiative\n+ Can't be surprised while conscious\n"
        #                        "+ No stealth advantage for attackers."
        #               }
        # pickle.dump(load_feats, open("feats_dict.p", "wb"))

    # Essential Methods
    # =========================================================
    def save(self):
        pickle.dump(self.stats, open("hero_info.p", "wb"))
        pickle.dump(self.feats_traits, open("feats_dict.p", "wb"))

    def set_stat(self, stat, value):
        if stat in self.stats.keys():
            try:
                self.stats[stat] = value
                if stat == "Max HP":
                    self.stats["Current HP"] = value
            except:
                print("[ER] Cannot modify ", stat, "...")
        else:
            print("[ER] ", stat, " does not exist!")

    def get_stat(self, stat):
        if self.stats.keys().__contains__(stat):
            return self.stats[stat]
        else:
            print("[ER] That stat is unavailable!")

    def calc_modifier(self, modifier):
        try:
            if 0 < self.stats[modifier] <= 20:
                return math.floor(self.stats[modifier] - 10 / 2)
            raise Exception
        except:
            print("[ER] Could not calculate modifier for", modifier)

    # Accessors
    # =========================================================
    # def get_name(self):
    #     return self.name

    # def get_id(self):
    #     return self.id

    # def get_role(self):
    #     return self.role

    # def get_level(self):
    #     return self.level

    # def get_race(self):
    #     return self.race

    # def get_background(self):
    #     return self.background

    # def get_alignment(self):
    #     return self.alignment

    # def get_base_stat(self, stat):
    #     return self.stat_block.get_stat(stat)

    def get_modifier(self, modifier):
        try:
            return self.modifier[modifier]
        except:
            print("[ER] Cannot retrieve", modifier, "modifier.")

    def get_passive_per(self):
        return self.modifier["wisdom"] + 10

    def get_ds_success(self):
        return self.ds_success

    def get_ds_fail(self):
        return self.ds_fail

    # def get_personality(self):
    #     return self.personality
    #
    # def get_ideals(self):
    #     return self.ideals
    #
    # def get_bonds(self):
    #     return self.bonds
    #
    # def get_flaws(self):
    #     return self.flaws
    #
    # def get_weapon(self):
    #     return self.held_weapon
    #
    # def get_armor(self):
    #     return self.worn_armor
    #
    def get_feat_name(self, index):
        return list(self.feats_traits.keys())[index]

    def get_feat_desc(self, name):
        return self.feats_traits[name]

    def get_feat_size(self):
        return len(self.feats_traits)

    def edit_feat(self, pair):
        self.feats_traits[pair[0]] = pair[1]

    # def get_prof(self, prof):
    #     for i in self.prof_langs:
    #         if i == prof:
    #             return self.prof_langs[i]
    #         else:
    #             return None

    # def get_item(self, item):
    #     for i in self.inventory:
    #         if i == item:
    #             return self.inventory[i]
    #         else:
    #             return None

    # def get_spell(self, spell):
    #     for i in self.spells:
    #         if i == spell:
    #             return self.spells[i]
    #         else:
    #             return None

    # Mutators
    # =========================================================
    # def set_name(self, string):
    #     self.name = string
    #
    # def set_id(self, num):
    #     self.id = num
    #
    # def set_role(self, string):
    #     self.role = string

    def level_up(self):
        if self.stats["level"] < 20:
            self.stats["level"] += 1
            self.save()

    def set_level(self, num):
        if 0 < num <= 20:
            self.stats["level"] = num
            return True
        return False

    # def set_race(self, string):
    #     self.race = string
    #
    # def set_background(self, string):
    #     self.background = string
    #
    # def set_alignment(self, string):
    #     self.alignment = string
    #
    # def set_base_stat(self, stat, num, face=None):
    #     self.stat_block.modify_stat(stat, num, face)
    #
    # def set_modifier(self, modifier, value):
    #     self.modifiers[modifier] = value
    #
    def ds_success(self):
        self.ds_success += 1

    def ds_fail(self):
        self.ds_fail += 1

    # def set_personality(self, string):
    #     self.personality = string
    #
    # def set_ideals(self, string):
    #     self.ideals = string
    #
    # def set_bonds(self, string):
    #     self.bonds = string
    #
    # def set_flaws(self, string):
    #     self.flaws = string
    #
    # def swap_weapon(self, swap):
    #     temp = self.get_item(swap)
    #     if temp is not None:
    #         self.inventory.append(self.held_weapon)
    #         self.held_weapon = temp
    #
    # def swap_armor(self, swap):
    #     temp = self.get_item(swap)
    #     if temp is not None:
    #         self.inventory.append(self.worn_armor)
    #         self.worn_armor = temp

    # def add_feat(self, name, desc, name_only):
    def add_feat(self, name, desc, original):
        if name:
            if not desc and name != original:
                self.feats_traits[name] = self.feats_traits[original]
                del self.feats_traits[original]
            elif desc and original and name != original:
                del self.feats_traits[original]
                self.feats_traits[name] = desc
            elif desc and not original:
                self.feats_traits[name] = desc
        if not name and desc:
            self.feats_traits[original] = desc

    # def add_prof(self, name, desc):
    #     self.prof_langs[name] = desc
    #
    # def add_to_inv(self, item):
    #     self.inventory.append(item)
    #
    # def add_spell(self, name, desc):
    #     self.spells[name] = desc



