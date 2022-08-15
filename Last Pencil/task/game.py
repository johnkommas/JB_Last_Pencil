# 1.
import random
names = ["John", "BoT"]


def get_number(text=''):
    try:
        number = int(input(text))
        if number <= 0:
            print("The number of pencils should be positive")
            return get_number()
    except ValueError:
        print("The number of pencils should be numeric")
        return get_number()
    return number


def pencils(numberOfPencils, text=''):
    accepted = [1, 2, 3]
    try:
        x = int(input(text))
        if x > numberOfPencils:
            print("Possible values: '1', '2' or '3'")
            print("Too many pencils were taken")
            return pencils(numberOfPencils)
        elif x in accepted:
            return x
        else:
            print("Possible values: '1', '2' or '3'")
            return pencils(numberOfPencils)
    except ValueError:
        print("Possible values: '1', '2' or '3'")
        return pencils(numberOfPencils)


def get_name(text=''):
    person = input(text)
    if person not in names:
        print(f"Choose between '{names[0]}' and '{names[1]}'")
        return get_name()
    else:
        return person


def bot_turn(pencils, text=''):
    print(text)
    if pencils in loosing_numbers:
        if pencils > 3:
            to_take = random.choice([1, 2, 3])
        else:
            to_take = 1
    else:
        current_list = [*range(1, pencils, 4)]
        closest_loosing = current_list[-1]
        to_take = pencils - closest_loosing
    print(to_take)
    return to_take


numberOfPencils = get_number("How many pencils would you like to use:\n")
loosing_numbers = [*range(1, numberOfPencils + 1, 4)]
who_goes_first = get_name(f"Who will be the first ({names[0]}, {names[1]}):\n")

while True:
    print(f'{"|" * numberOfPencils}')
    if who_goes_first == names[0]:
        x = pencils(numberOfPencils, f"{names[0] if who_goes_first == names[0] else names[1]}'s turn: \n")
    else:
        x = bot_turn(numberOfPencils, f"{names[0] if who_goes_first == names[0] else names[1]}'s turn:")
    who_goes_first = (names[1] if who_goes_first == names[0] else names[0])
    if x == numberOfPencils:
        print(f"{who_goes_first} won!")
        break
    else:
        numberOfPencils -= x

