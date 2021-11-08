from random import randrange


##### CLASSES #####
class CustomDice:
    dice = {
        1: {"d6": "◻", "d12": "◻"},
        2: {"d6": "🤔😫", "d12": "◻"},
        3: {"d6": "🤔", "d12": "🤔"},
        4: {"d6": "👏😫", "d12": "🤔"},
        5: {"d6": "👏", "d12": "🤔"},
        6: {"d6": "🎆😫", "d12": "👏😫"},
        7: {"d12": "👏😫"},
        8: {"d12": "👏"},
        9: {"d12": "👏"},
        10: {"d12": "👏🤔"},
        11: {"d12": "🎆😫"},
        12: {"d12": "🎆"}
    }

    def __init__(self, ring: int, skill: int):
        self.ring = int(ring)
        self.skill = int(skill)

    def roll(self):
        values = {
            "ring": self.ring,
            "skill": self.skill
        }

        results = {
            "ring": [],
            "skill": []
        }

        for key, value in values.items():
            for i in range(1, value+1):
                dieface = randrange(
                    1, 7) if key == "ring" else randrange(1, 13)
                diekey = "d6" if key == "ring" else "d12"
                results[key].append(self.dice[dieface][diekey])

        return results

    def format(self, **kwargs):
        rolled_dice = kwargs

        [rolled_dice.update({key: [f"[{face}]" for face in value]})
         for key, value in rolled_dice.items()]
        [rolled_dice.update({key: ', '.join(value)})
         for key, value in rolled_dice.items()]
        rolled_dice = f"Ring dice: {rolled_dice['ring']}\nSkill dice: {rolled_dice['skill']}"

        return rolled_dice
