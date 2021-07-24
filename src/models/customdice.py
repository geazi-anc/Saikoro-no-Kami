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
def convert(**kwargs):

    try:
        [kwargs.update({key: int(value)}) for key, value in kwargs.items()]

    except ValueError:
        print("Um dos argumentos não é válido")

    else:
        return kwargs


def dice_roller(**kwargs):
    results = {
        "d6": [],
        "d12": []
    }

    for key, value in kwargs.items():
        for i in range(1, value+1):
            face = randrange(1, 7) if key == "d6" else randrange(1, 13)
            results[key].append(dice[face][key])

    return results


def format(**kwargs):
    [kwargs.update({key: [f"[{face}]" for face in value]})
     for key, value in kwargs.items()]
    [kwargs.update({key: ", ".join(value)}) for key, value in kwargs.items()]
    
    return kwargs
