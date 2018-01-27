class Unit:
    def __init__(self, name, isGround, isBlack, total_health, black_dice, red_dice, current_damage):
        self.name = name
        self.isGround = isGround
        self.isBlack = isBlack
        self.total_health = total_health
        self.black_dice = black_dice
        self.red_dice = red_dice
        self.current_damage = current_damage

    def __str__(self):
        return "Name: {}, health: {}".format(
            self.name, self.current_damage)

class Rebels(Unit):
    number_of_units = 0
    def __init__(self, name, isGround, isBlack, total_health, black_dice, red_dice, current_damage):
        super().__init__(name, isGround, isBlack, total_health, black_dice, red_dice, current_damage)
        Rebels.number_of_units += 1

RS_units_dict = {
    "X-wings" : 0,
    "U-wings" : 0,
}

test = 2
if test:
    for unit in RS_units_dict:
        not_accepted = True
        while not_accepted:
            try:
                user_noUnits = int(input(unit))
                not_accepted = False
            except:
                print("not a valid number of units")
        number_of_units_dict = {}
        number_of_units_dict["Initial_Number"] = user_noUnits

        if unit == "X-wings":
            number_of_units_dict["objects"] = [Rebels(unit, 0, 1, 1, 1, 0, 0) for x in range(user_noUnits)]

        RS_units_dict[unit] = number_of_units_dict

    print(RS_units_dict)

for obj in RS_units_dict["X-wings"]["objects"]:
    print(obj)

rebx = Rebels("Xwing", 0, 1, 1, 1, 0, 0)
print()
print(rebx)

