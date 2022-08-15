# 1.
import random
from termcolor import colored


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


def bot_turn(remaining_pencils, text=''):
    """
    Το BoT κάθε φορά που έιναι η σειρά του να παίξει ελέγχει αν βρίσκεται
    σε θέση νικητή.

    Αν ναι, τότε παίρνει τόσα στυλό όσα χρειάζεται για συνεχίζει
    να κερδίζει

    Αν όχι, τότε παίρνει ένα τυχαίο αριθμό στυλό 1, 2 ή 3
    ελπίζοντας ο αντίπαλος παίχτης να πάρει λάθος αριθμό.

    :param remaining_pencils:
    :param text:
    :return:
    """
    texts = ["I Will Crush You Down!!",
             "You Ain't Winning That!!",
             "Hey, I am Going to Win That Game, You Know That don't You?",
             "I Am Pretty Sure You Are Lost",
             "Haha, I See You Picking Random Pencils",
             "Whoooooha, ha ha ha ha !!!",
             "Watch And Learn Babe",
             "Are You Sure You Want to Continue?, I am Winning Here!!",
             "OMG That's an Easy and Fun Win",
             "Win Win, o Yeah i still Win",
             "Oups, My Turn, Time To Win Again, haha",
             "I Just Love That ... Winning Style",
             "I Can Keep Doing it All Day",
             "You Can't Beat Me, You Know",
             "I Thing You Just ... Love Loosing Games or smth?"]
    print(text)
    if remaining_pencils in loosing_numbers:
        print("BoT is Guessing and Picks: ", end='')
        if remaining_pencils > 3:
            to_take = random.choice([1, 2, 3])
        else:
            to_take = 1
    else:
        print(f"BoT Says: {random.choice(texts)}. I Will Take: ", end='')
        current_list = [*range(1, remaining_pencils, 4)]
        closest_loosing = current_list[-1]
        to_take = remaining_pencils - closest_loosing
    print(to_take)
    return to_take

# Get Player Name
names = ['BoT']
names.append(input("Give Me Your Name: "))

# Ask How Many Pencils Will Be In The Start Of The Game
numberOfPencils = get_number("How many pencils would you like to use:")

# Calculate the Loosing Positions based on the number given above (1, 4, 9, 13 ...)
loosing_numbers = [*range(1, numberOfPencils + 1, 4)]

# Visualize if The First Player will (🔴)Lose or (🟢)Win
if numberOfPencils in loosing_numbers:
    print("🔴: ", end='')
else:
    print("🟢: ", end='')

# Ask Who Starts The Game
players_turn = get_name(f"Who will be the first ({names[0]}, {names[1]}):")

while True:
    # SIMPLE OUTPUT
    # print(f'{"|" * numberOfPencils}')

    # COLORED OUTPUT (Visualize Win Strat)
    for i in range(numberOfPencils):
        print(colored("|", "red") if i + 1 in loosing_numbers else colored("|", "green"), end='')
    print(f" : => ✏️Pencils Left: ({numberOfPencils})")

    # CHECK IF IT IS BoT TURN OR NOT
    if players_turn == names[1]:
        x = pencils(numberOfPencils, f"{names[1] if players_turn == names[1] else names[0]}'s turn: ")
    else:
        x = bot_turn(numberOfPencils, f"{names[1] if players_turn == names[1] else names[0]}'s turn: ")

    # CHANGE PLAYER
    players_turn = (names[1] if players_turn == names[0] else names[0])

    # CHECK WINNER
    if x == numberOfPencils:
        print(f"{players_turn} won!")
        break
    else:
        numberOfPencils -= x
