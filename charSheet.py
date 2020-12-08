from stat_block import StatBlock
import math
import pickle


class CharSheet:
    def __init__(self):
        try:
            self.stats = pickle.load(open("hero_info.p", "rb"))
        except:
            self.stats = StatBlock().get()
            pickle.dump(self.stats, open("hero_info.p", "wb"))

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
        self.feats_traits = pickle.load(open("feats_dict.p", "rb"))

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

    def get_feat_name(self, index):
        return list(self.feats_traits.keys())[index]

    def get_feat_desc(self, name):
        return self.feats_traits[name]

    def get_feat_size(self):
        return len(self.feats_traits)

    def edit_feat(self, pair):
        self.feats_traits[pair[0]] = pair[1]

    # Mutators
    # =========================================================
    def level_up(self):
        if self.stats["level"] < 20:
            self.stats["level"] += 1
            self.save()

    def set_level(self, num):
        if 0 < num <= 20:
            self.stats["level"] = num
            return True
        return False

    def ds_success(self):
        self.ds_success += 1

    def ds_fail(self):
        self.ds_fail += 1

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
