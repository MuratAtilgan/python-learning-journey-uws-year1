class Team:
    def __init__(self,name,colour,star_player):
        self.name=name
        self.colour=colour
        self.star_player=star_player
    
    def get_name(self):
        return self.name
    
    def get_colour(self):
        return self.colour
    
    def get_star_player(self):
        return self.star_player
    
    def display_team_info(self):
        print(f"Team:\t\t{self.get_name()}")
        print(f"Sport:\t\t{self.sport}")
        print(f"Colour:\t\t{self.get_colour()}")
        print(f"Star Player:\t{self.get_star_player()}")
    
class Football(Team):

    sport="Football"

    #def __init__(self, name, colour,star_player):
        #super().__init__(name, colour)
        #self.star_player=star_player

    #def display_team_info(self):
        #print(f"Team:\t\t{self.name}")
        #print(f"Sport:\t\t{self.sport}")
        #print(f"Colour:\t\t{self.colour}")
        #print(f"Star Player:\t{self.star_player}")

class Rugby(Team):

    sport="Rugby"

    #def __init__(self, name, colour,flyhalf):
        #super().__init__(name, colour)
        
        #self.flyhalf=flyhalf

    #def display_team_info(self):
        #print(f"Team:\t\t{self.name}")
        #print(f"Sport:\t\t{self.sport}")
        #print(f"Colour:\t\t{self.colour}")
        #print(f"Flyhalf:\t\t{self.flyhalf}")


class Ice_Hockey(Team):

    sport="Ice_Hockey"

    #def __init__(self, name, colour,goalie):
        #super().__init__(name, colour)

        #self.goalie=goalie

    #def display_team_info(self):
        #print(f"Team:\t\t{self.name}")
        #print(f"Sport:\t\t{self.sport}")
        #print(f"Colour:\t\t{self.colour}")
        #print(f"Goalie:\t\t{self.goalie}")


class Shinty(Team):

    sport="Shinty"

    #def __init__(self, name, colour,captain):
        #super().__init__(name, colour)

        #self.captain=captain

    #def display_team_info(self):
        #print(f"Team:\t\t{self.name}")
        #print(f"Sport:\t\t{self.sport}")
        #print(f"Colour:\t\t{self.colour}")
        #print(f"Captain:\t\t{self.captain}")


##MENU

def select():
    print()
    print("="*75)
    print("<:::> TEAM DATABASE <:::>")
    print("="*75)
    print("1 ..... FOOTBALL")
    print("2 ..... RUGBY")
    print("3 ..... ICE HOCKEY")
    print("4 ..... SHINTY")
    print("5 ..... VIEW ALL TEAMS")
    print("6 ..... QUIT PROGRAM")
    print("="*75)
    option = input("Select: ")
    print()
    return option

def quit_program():
    print("="*75)
    print("<:::> GOOD BYE <:::>")
    print("="*75)

def invalid_entry():
    print("Invalid ENTRY!!! Please select 1,2,3,4,5 and 6")


teams=[]

selection=select()


##MAIN PROGRAM

while True:
    
    if selection == "1":
        name=input("Enter the Team:\t\t")
        colour=input("Enter the colours:\t")
        star_player=input("Who is the star player:\t")    
        teams.append(Football(name,colour,star_player))   
        print()
        print("="*50)
        print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>")  ##confirmation message
        print()
        teams[-1].display_team_info()   ##Calls method to show all details
        print("="*50)

    elif selection == "2":
        name=input("Enter the Team:\t\t")
        colour=input("Enter the colours:\t")
        star_player=input("Who is the flyhalf:\t")    
        teams.append(Rugby(name,colour,star_player))   
        print()
        print("="*50)
        print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>") 
        print() 
        teams[-1].display_team_info()   
        print("="*50)

    elif selection == "3":
        name=input("Enter the Team:\t\t")
        colour=input("Enter the colours:\t")
        star_player=input("Who is the goalie:\t")    
        teams.append(Ice_Hockey(name,colour,star_player))   
        print()
        print("="*50)
        print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>") 
        print() 
        teams[-1].display_team_info()   
        print("="*50)

    
    elif selection == "4":
        name=input("Enter the Team:\t\t")
        colour=input("Enter the colours:\t")
        star_player=input("Who is the captain:\t")    
        teams.append(Shinty(name,colour,star_player))   
        print()
        print("="*50)
        print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>")  
        print()
        teams[-1].display_team_info()   
        print("="*50)

    elif selection == "5":
        print("="*75)
        print("ALL TEAMS")
        print("="*75)
        for team in teams:
            team.display_team_info()
        print("="*75)

    
    elif selection == "6":
        quit_program()
        break

    else:
        invalid_entry()

    selection=select()






    

    