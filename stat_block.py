from random import randint


class StatBlock:
    def __init__(self):
        hero_id = randint(000, 999)
        # dictionary of all stats
        self.stats = {
            # Character Details
            "id": hero_id,
            "name": "Hero",
            "level": 1,
            "role": "",
            "race": "",
            "alignment": "",

            # Character Stats
            "armor class": 0,
            "speed": 0,
            "current hp": 0,
            "max hp": 0,
            "hit dice": 0,

            # Misc Stats
            "inspiration": 0,
            "proficiency Bonus": 0,

            # Ability Scores
            "strength": 1,
            "dexterity": 1,
            "constitution": 1,
            "wisdom": 1,
            "intellect": 1,
            "charisma": 1,

            # Skills
            "acrobatics": -5,
            "animal Handling": -5,
            "arcana": -5,
            "athletics": -5,
            "deception": -5,
            "history": -5,
            "insight": -5,
            "intimidation": -5,
            "investigation": -5,
            "medicine": -5,
            "nature": -5,
            "perception": -5,
            "performance": -5,
            "persuasion": -5,
            "religion": -5,
            "sleight Of Hand": -5,
            "stealth": -5,
            "survival": -5
        }

    def get(self):
        return self.stats
