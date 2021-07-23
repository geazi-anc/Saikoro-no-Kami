from random import randrange


### VARIABLES ###
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


### FUNCTIONS ###
def convert(rolled_dice):
    dicepool = {}

    try:
        rolled_dice = [int(face) for face in rolled_dice.split(" ")]

        dicepool["d6"] = rolled_dice[0]
        dicepool["d12"] = rolled_dice[1]

    except ValueError:
        print("Um dos argumentos não é válido")

    except IndexError:
        print("É necessário dois argumentos.")

    else:
        return dicepool


def dice_roller(dicepool):
    results = {
        "d6": [],
        "d12": []
    }

    for key, value in dicepool.items():
        for i in range(1, value+1):
            face = randrange(1, 7) if key == "d6" else randrange(1, 13)
            results[key].append(dice[face][key])

    return results
