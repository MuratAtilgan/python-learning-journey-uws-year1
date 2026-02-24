import random

suspects = ["Miss Scarlet", "Prof Plum", "Rev Green", "Colonel Mustard", "Mrs Peacock", "Mrs White"]
rooms    = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
weapons  = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Spanner"]


class guilty:

    def __init__(self):
        self.__murderer       = random.choice(suspects)
        self.__scene_of_crime = random.choice(rooms)
        self.__murder_weapon  = random.choice(weapons)

    def display_answer(self):
        print()
        print(f"Answer: {self.__murderer} - {self.__scene_of_crime} - {self.__murder_weapon}")
        print()

    def check_solution(self, murderer, scene_of_crime, murder_weapon):
        print()
        if (murderer == self.__murderer and
                scene_of_crime == self.__scene_of_crime and
                murder_weapon  == self.__murder_weapon):
            print("Well done Sherlock, you nailed it!")
            print()
            return True
        else:
            print("="*65)
            print("Wrong — you're more sloth than sleuth!")
            print("="*65)
            print()
            ##show player which parts of their guess were correct or wrong
            if murderer == self.__murderer:
                print("Suspect  ......  Correct")
            else:
                print("Suspect  ......  Wrong")
            if scene_of_crime == self.__scene_of_crime:  
                print("Room     ......  Correct")
            else:
                print("Room     ......  Wrong")
            if murder_weapon == self.__murder_weapon:   
                print("Weapon   ......  Correct")
            else:
                print("Weapon   ......  wrong")
            print()
            return False


def get_choice(max_number):          ##error handling <=-=>keep asking until valid number entered
    while True:
        try:
            choice=int(input(">>> "))
            if 1 <= choice <= max_number:
                return choice
            else:
                print()
                print(f"  Please enter a number between 1 and {max_number}")
                print()
        except ValueError:
            print(f"  Please enter a number between 1 and {max_number}")
            print()


def am_I_correct():
    print()
    print("Who committed the murder?")
    print()
    for i in range(6):
        print(f"  {i+1} ..... {suspects[i]}")
    print()
    murderer_choice = get_choice(6)
    murderer = suspects[murderer_choice -1]

    print()
    print("Where was the murder committed?")
    print()
    for j in range(9):
        print(f"  {j+1} ..... {rooms[j]}")
    print()
    room_choice    = get_choice(9)
    scene_of_crime = rooms[room_choice -1]

    print()
    print("Which weapon was used?")
    print()
    for k in range(6):
        print(f"  {k+1} ..... {weapons[k]}")
    print()
    weapon_choice = get_choice(6)
    murder_weapon = weapons[weapon_choice -1]

    return solution.check_solution(murderer, scene_of_crime, murder_weapon)




solution = guilty()              ##create the secret solution object
##solution.display_answer()     ##secret is now hidden — encapsulation!

attempts=0                    ##count how many guesses the player makes
solved=False                ##becomes True when player guesses correctly

while not solved and attempts < 3:
    attempts += 1
    solved=am_I_correct()     ##ask player to guess —returns True if correct
    if not solved and attempts <3:
        print(f"Guess {attempts} used and {3-attempts} attempts remain!")
        print()

if solved:
    print("="*65)
    if attempts == 1:   ##if guess success in the first guess
        print()
        print("Well done! Solved it on the first guess!")
    else:
        print()
        print(f"You solved it in {attempts} guesses!") ##if guess within 3 guess 
    print()
    print("="*65)
else:
    print("="*65)
    print()
    print("3 guesses used — murderer ran away!")
    solution.display_answer()   ##reveal the answer only at game over
    print("="*65)
print()
