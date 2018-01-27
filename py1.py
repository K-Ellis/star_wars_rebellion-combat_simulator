import random

RS_units_dict = {
    "X-wings": {
        "Initial": 0,
        "Current": 0,
        "Black": 1,
        "Red": 0,
        "Health": 1,
        "Damage": 0
    }
                    ,
    "U-wings": {
        "Initial": 0,
        "Current": 0,
        "Black": 0,
        "Red": 1,
        "Health": 1,
        "Damage": 0
    }
}

test = 2
if test:
    for unit in RS_units_dict:
        not_accepted = True
        while not_accepted:
            try:
                user_noUnits = int(input("%s: " % unit))
                not_accepted = False
            except:
                print("not a valid number of units")

        RS_units_dict[unit]["Initial"] = user_noUnits
        RS_units_dict[unit]["Current"] = user_noUnits

    print(RS_units_dict)

def get_dice(unit_dict):
    black_d, red_d = 0, 0
    for unit in unit_dict:
        black_d += unit_dict[unit]["Black"] * unit_dict[unit]["Current"]
        red_d += unit_dict[unit]["Red"] * unit_dict[unit]["Current"]
    if black_d > 5:
        black_d = 5
    if red_d > 5:
        red_d = 5
    return black_d, red_d

print(get_dice(RS_units_dict))

def roll_dice(num_dice):
    for i in range(num_dice):
        print(random.randint(1,7))

    # return miss, hit, direct, double