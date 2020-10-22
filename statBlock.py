class StatBlock:

    def __init__(self):
        # dictionary of all stats
        self.stats = {
            # Misc Stats
            "initiative": 0,
            "inspiration": 0,
            "profBonus": 0,
            "weight": 0,
            "tileSize": 0,

            # Character Stats
            "armorClass": 0,
            "speed": 0,
            "currentHP": 0,
            "maxHP": 0,
            "hitDice": [0, 0],

            # Ability Scores
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "wisdom": 0,
            "intellect": 0,
            "charisma": 0,

            # Skills
            "acrobatics": 0,
            "animalHandling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleightOfHand": 0,
            "stealth": 0,
            "survival": 0
        }

    def modify_stat(self, stat, num, faces=None):
        if faces is None:
            if stat == "hitDice":
                self.stats[stat][0] = num
            else:
                self.stats[stat] = num
        elif stat == "hitDice":
            self.stats[stat][0:2] = [num, faces]
        else:
            print("invalid operation: modify_stat")

    def get_stat(self, stat):
        return self.stats.get(stat, default=None)
