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
            "Armor Class": 0,
            "Speed": 0,
            "Current HP": 0,
            "Max HP": 0,
            "Hit Dice": 0,

            # Misc Stats
            "Inspiration": 0,
            "Proficiency Bonus": 0,

            # Ability Scores
            "Strength": 1,
            "Dexterity": 1,
            "Constitution": 1,
            "Wisdom": 1,
            "Intellect": 1,
            "Charisma": 1,

            # Skills
            "Acrobatics": -5,
            "Animal Handling": -5,
            "Arcana": -5,
            "Athletics": -5,
            "Deception": -5,
            "History": -5,
            "Insight": -5,
            "Intimidation": -5,
            "Investigation": -5,
            "Medicine": -5,
            "Nature": -5,
            "Perception": -5,
            "Performance": -5,
            "Persuasion": -5,
            "Religion": -5,
            "Sleight Of Hand": -5,
            "Stealth": -5,
            "Survival": -5
        }

    def get(self):
        return self.stats
