# 1.
import random
from termcolor import colored
import time

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


def pencils(number_of_pencils, text=''):
    accepted = [1, 2, 3]
    try:
        player_input = int(input(text))
        if player_input > number_of_pencils:
            print("Possible values: '1', '2' or '3'")
            print("Too many pencils were taken")
            return pencils(number_of_pencils)
        elif player_input in accepted:
            return player_input
        else:
            print("Possible values: '1', '2' or '3'")
            return pencils(number_of_pencils)
    except ValueError:
        print("Possible values: '1', '2' or '3'")
        return pencils(number_of_pencils)


def get_name(names, text=''):
    person = input(text)
    if person not in names:
        print(f"Choose between '{names[0]}' and '{names[1]}'")
        return get_name()
    else:
        return person


def bot_turn(name, loosing_numbers, remaining_pencils, text=''):
    """
    Το BoT κάθε φορά που είναι η σειρά του να παίξει ελέγχει αν βρίσκεται
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
             "Ops, My Turn, Time To Win Again, haha",
             "I Just Love That ... Winning Style",
             "I Can Keep Doing it All Day",
             "You Can't Beat Me, You Know",
             "I Thing You Just ... Love Loosing Games or smth?"]
    print(text)
    # time.sleep(2)
    if remaining_pencils in loosing_numbers:
        print(f"{name} is Guessing and Picks: ", end='')
        if remaining_pencils > 3:
            to_take = random.choice([1, 2, 3])
        else:
            to_take = 1
    else:
        print(f"{name} Says: {random.choice(texts)}. I Will Take: ", end='')
        current_list = [*range(1, remaining_pencils, 4)]
        closest_loosing = current_list[-1]
        to_take = remaining_pencils - closest_loosing
    # time.sleep(1)
    print(to_take)
    return to_take


def main():
    print("++++++++++++++ NEW GAME: ++++++++++++++")
    # Get Player Name
    names = ['BoT', input("Give Me Your Name: ")]
    # Ask How Many Pencils Will Be In The Start Of The Game
    numberOfPencils = get_number("How many pencils would you like to use:")

    # Calculate the Loosing Positions based on the number given above (1, 4, 9, 13 ...)
    loosing_numbers = [*range(1, numberOfPencils + 1, 4)]

    # IF Players Name is HackMe or HackBot then You Get A Visual Win
    version = 0
    if names[1].upper() == 'HACKME' or names[1].upper() == 'HACKBOT':
        version = 1
        # Visualize if The First Player will (🔴)Lose or (🟢)Win
        # if Red give it to BoT
        # if Green Play First
        if numberOfPencils in loosing_numbers:
            print("🔴: ", end='')
        else:
            print("🟢: ", end='')

    # Ask Who Starts The Game
    players_turn = get_name(names, f"Who will be the first ({names[0]}, {names[1]}):")

    while True:

        if version:
            # COLORED OUTPUT (Visualize Win Strat) Enabled only if your name is HackMe or HackBot
            # To Win Just Count Green Pencils Until Red and Pick THEM.
            for i in range(numberOfPencils):
                print(colored("|", "red") if i + 1 in loosing_numbers else colored("|", "green"), end='')
        else:
            # SIMPLE OUTPUT
            print(f'{"|" * numberOfPencils}', end='')

        print(f" : => ✏️Pencils Left: ({numberOfPencils})")

        # CHECK IF IT IS BoT TURN OR NOT
        if players_turn.upper() == 'HACKBOT':
            x = bot_turn(players_turn, loosing_numbers, numberOfPencils,
                         f"{names[1] if players_turn == names[1] else names[0]}'s turn: ")
        elif players_turn == names[1]:
            x = pencils(numberOfPencils, f"{names[1] if players_turn == names[1] else names[0]}'s turn: ")
        else:
            x = bot_turn(players_turn, loosing_numbers, numberOfPencils, f"{names[1] if players_turn == names[1] else names[0]}'s turn: ")

        # CHANGE PLAYER
        players_turn = (names[1] if players_turn == names[0] else names[0])

        # CHECK WINNER
        if x == numberOfPencils:
            print(f"{players_turn} won!")
            break
        else:
            numberOfPencils -= x


while True:
    main()
    if input("Continue: (Y) or (N): ").upper() == "N":
        print("GAME OVER")
        break

