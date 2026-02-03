class suspect:
    def __init__(self, title, name, location,weapon):
        self.title = title
        self.name = name
        self.location = location
        self.weapon=weapon

    def who_are_you(self):
        print()
        print(f"I am {self.title:10} {self.name:10}")
        print()

    def where_are_you(self):
        print()
        print(f"{self.title:10} {self.name:10}is in the\t{self.location:15}")
        print()
    
    def what_weapon(self):
        print()
        print(f"{self.title:10} {self.name:10}has the\t{self.weapon:15}")
        print()

    def change_location(self, location):
        self.location = location

    def change_weapon(self,weapon):
        self.weapon=weapon

players = []

players.append(suspect("Proffessor", "Plum", "Kitchen","Candlestick"))
players.append(suspect("Mrs.","White","Lounge","Lead Pipe"))
players.append(suspect("Mr.","Body","Ballroom","Rope"))

for player in players:
    player.where_are_you()
    player.what_weapon()

print("="*75)
print("AFTER CHANGES")
print("="*75)

players[0].change_location("Conservatory")
players[1].change_location("Hall")
players[2].change_location("Dining Room")   


players[0].change_weapon("Dagger")
players[1].change_weapon("Revolver")
players[2].change_weapon("Lead Pipe") 

for player in players:
    player.where_are_you()
    player.what_weapon()