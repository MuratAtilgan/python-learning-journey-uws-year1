import random

class Player:
    
    def __init__(self,player_name):
        self.player_name=player_name
        self.character= Suspect()

    
    def display(self):
        print()
        print("="*65)
        print()
        print(f"Player:\t\t{self.player_name}")
        print()
        print(f"Character:\t{self.character.get_suspect()}")
        print()

class Suspect:

    def __init__(self):
         suspects=["Miss Scarlett (red)","Colonel Mustard(yellow)","Mrs. White (white)","Mr. Green (green)","Mrs. Peacock (blue)","Professor Plum (purple)"]
         
         self.sus_name=random.choice(suspects)

    def get_suspect(self):
        
        return self.sus_name
    

p1=Player("Muratti")
p2=Player("Jordan")
p3=Player("Shaun")
p4=Player("Joann")

p1.display()
p2.display()
p3.display()
p4.display()



