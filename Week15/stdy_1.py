import random

class Player:
    
    def __init__(self,player_name):
        self.player_name=player_name
        self.character= Suspect()
        self.place= Location()

    
    def display(self):
        print()
        print("="*65)
        print()
        print(f"Player:\t\t{self.player_name}")
        print()
        print(f"Character:\t{self.character.get_suspect()}")
        print()
        print(f"Location:\t{self.place.get_location()}")
        print()
        print("="*65)
        print()
        print()

class Suspect:

    def __init__(self):
         suspects=["Miss Scarlett (red)","Colonel Mustard(yellow)","Mrs. White (white)","Mr. Green (green)","Mrs. Peacock (blue)","Professor Plum (purple)"]
         
         self.sus_name=random.choice(suspects)

    def get_suspect(self):
        
        return self.sus_name
    
class Location:

    def __init__(self):
        
        locations=["the Kitchen","Ballroom","Conservatory","Dining Room","Billiard Room","Library","Lounge","Hall","Study"]

        self.sus_loc=random.choice(locations)

    def get_location(self):

        return self.sus_loc
    

p1=Player("Muratti")
p2=Player("Jordan")
p3=Player("Shaun")
p4=Player("Joann")

p1.display()
p2.display()
p3.display()
p4.display()



