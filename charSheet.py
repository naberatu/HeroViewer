"""
AUTHOR:         Nader K. Atout
BASED ON:       Dungeons & Dragons by Wizards of the Coast
USING ASSETS:   New Rocker Font by Pablo Impallari
                Minimalist Dragon Background from wallpaperaccess.com
                Program Scroll Icon from game-icons.net
"""

from stat_block import StatBlock
import math
import pickle


class CharSheet:
    def __init__(self):

        # Fills in User data (HP, Attributes, etc).
        try:
            self.stats = pickle.load(open("hero_info.p", "rb"))
        except:
            self.stats = StatBlock().get()
            self.set_stat("AC", self.stats["AC"])
            pickle.dump(self.stats, open("hero_info.p", "wb"))

        # Fills in Feature list.
        try:
            self.feats_traits = pickle.load(open("feats_dict.p", "rb"))
        except:
            self.feats_traits = {"Warrior": "Once per short rest, you can take a bonus action.",
                                 "Tamer": "Grants +2 Nature",
                                 "Alert": "+ Gain +5 Initiative\n+ Can't be surprised while conscious\n"
                                            "+ No stealth advantage for attackers."
                                 }
            pickle.dump(self.feats_traits, open("feats_dict.p", "wb"))

    # =========================================================
    # Essential Methods
    # =========================================================

    # Stores all current data into the appropriate file.
    def save_all(self):
        pickle.dump(self.stats, open("hero_info.p", "wb"))
        pickle.dump(self.feats_traits, open("feats_dict.p", "wb"))

    # Modifies a given stat to hold a given value.
    def set_stat(self, stat, value):
        numeric_stats = ["level"] + list(self.stats.keys())[6:]
        try:
            if stat in numeric_stats:
                value = int(value)
                if 0 < value <= 20 or stat in self.get_block() or stat == "Max HP":
                    if stat == "AC":
                        self.stats[stat] = value + self.get_modifier("dexterity")
                    elif stat == "HP" and value > self.stats["Max HP"]:
                        pass
                    else:
                        self.stats[stat] = value
                        if stat == "Max HP":
                            self.stats["HP"] = value
            else:
                self.stats[stat] = value
                if stat == "race":
                    if value == "Dwarf" or value == "Gnome" or value == "Halfling":
                        self.stats["Spd"] = 20
                    else:
                        self.stats["Spd"] = 30

            pickle.dump(self.stats, open("hero_info.p", "wb"))
        except:
            print("[ER] Cannot modify", stat, "...")

    # Returns the value of a given stat.
    def get_stat(self, stat):
        if self.stats.keys().__contains__(stat):
            return self.stats[stat]
        else:
            print("[ER] That stat is unavailable!")

    # =========================================================
    # Accessors
    # =========================================================
    def get_modifier(self, modifier):
        try:
            return math.floor((self.stats[modifier] - 10) / 2)
        except:
            print("[ER] Cannot retrieve", modifier, "modifier.")

    def get_feat_name(self, index):
        return list(self.feats_traits.keys())[index]

    def get_feat_desc(self, name):
        return self.feats_traits[name]

    def get_feat_size(self):
        return len(self.feats_traits)

    def get_attributes(self):
        return list(self.stats.keys())[13:19]

    def get_skills(self):
        return list(self.stats.keys())[19:]

    def get_block(self):
        return list(self.stats.keys())[7:11]

    # =========================================================
    # Mutators
    # =========================================================

    # Increments level by 1.
    def level_up(self):
        if self.stats["level"] < 20:
            self.stats["level"] += 1
            pickle.dump(self.stats, open("hero_info.p", "wb"))

    # Add or edit a given feature.
    def add_feat(self, name, desc, original, new_entry):
        success = False
        if new_entry:
            self.feats_traits[name] = desc
            success = True
        elif name:
            if not desc and name != original:
                self.feats_traits[name] = self.feats_traits[original]
                del self.feats_traits[original]
                success = True
            elif desc and original and name != original:
                del self.feats_traits[original]
                self.feats_traits[name] = desc
                success = True
            elif desc and not original:
                self.feats_traits[name] = desc
                success = True
        elif not name and desc:
            self.feats_traits[original] = desc
            success = True

        if success:
            pickle.dump(self.feats_traits, open("feats_dict.p", "wb"))

    # Deletes a given feature.
    def del_feat(self, name):
        try:
            del self.feats_traits[name]
            pickle.dump(self.feats_traits, open("feats_dict.p", "wb"))
        except:
            print("[ER] Could not delete", name)
