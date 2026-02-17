class Team:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    
    def get_name(self):
        return self.name
    
    def get_colour(self):
        return self.colour
    
class Football(Team):

    sport="Football"

    def __init__(self, name, colour,star_player):
        super().__init__(name, colour)
        self.star_player=star_player

    def display_team_info(self):
        print(f"Team:\t\t{self.name}")
        print(f"Sport:\t\t{self.sport}")
        print(f"Colour:\t\t{self.colour}")
        print(f"Star Player:\t{self.star_player}")

class Rugby(Team):

    sport="Rugby"

    def __init__(self, name, colour,flyhalf):
        super().__init__(name, colour)
        
        self.flyhalf=flyhalf

    def display_team_info(self):
        print(f"Team:\t\t{self.name}")
        print(f"Sport:\t\t{self.sport}")
        print(f"Colour:\t\t{self.colour}")
        print(f"Flyhalf:\t{self.flyhalf}")


class Ice_Hockey(Team):

    sport="Ice_Hockey"

    def __init__(self, name, colour,goalie):
        super().__init__(name, colour)

        self.goalie=goalie

    def display_team_info(self):
        print(f"Team:\t\t{self.name}")
        print(f"Sport:\t\t{self.sport}")
        print(f"Colour:\t\t{self.colour}")
        print(f"Goalie:\t\t{self.goalie}")


class Shinty(Team):

    sport="Shinty"

    def __init__(self, name, colour,captain):
        super().__init__(name, colour)

        self.captain=captain

    def display_team_info(self):
        print(f"Team:\t\t{self.name}")
        print(f"Sport:\t\t{self.sport}")
        print(f"Colour:\t\t{self.colour}")
        print(f"Captain:\t{self.captain}")


class Holiday:
    
    def __init__(self, destination, duration,resort):
        self.destination = destination
        self.duration = duration
        self.resort=resort

    def get_destination(self):
        
        return self.destination
    
    def get_duration(self):

        return self.duration
    
    def get_resort(self):

        return self.resort
    
    def display_holiday_info(self):

        print(f"Holiday:\t\t{self.holiday_type}")
        print(f"Destination:\t\t{self.destination}")
        print(f"Resort:\t\t\t{self.resort}")
        print(f"Duration:\t\t{self.duration}")

       

class Beach(Holiday):
    
    holiday_type = "Beach"

    


class Ski(Holiday):
    
    holiday_type = "Ski"


class Space(Holiday):

    holiday_type = "Space"

       

def main_menu():
    print("1 ..... SPORTS")
    print("2 ..... HOLIDAYS")
    print("3 ..... QUIT")
    return input("Select: ")

def sports_program():
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
            flyhalf=input("Who is the flyhalf:\t")    
            teams.append(Rugby(name,colour,flyhalf))   
            print()
            print("="*50)
            print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>") 
            print() 
            teams[-1].display_team_info()   
            print("="*50)

        elif selection == "3":
            name=input("Enter the Team:\t\t")
            colour=input("Enter the colours:\t")
            goalie=input("Who is the goalie:\t")    
            teams.append(Ice_Hockey(name,colour,goalie))   
            print()
            print("="*50)
            print(f"<::> {teams[-1].__class__.__name__} TEAM ADDED SUCCESSFULLY <::>") 
            print() 
            teams[-1].display_team_info()   
            print("="*50)

        elif selection == "4":
            name=input("Enter the Team:\t\t")
            colour=input("Enter the colours:\t")
            captain=input("Who is the captain:\t")    
            teams.append(Shinty(name,colour,captain))   
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
       
    

def holiday_program():

    
    def select():
        print()
        print("="*75)
        print("<:::> HOLIDAY DATABASE <:::>")
        print("="*75)
        print("1 ..... BEACH")
        print("2 ..... SKI")
        print("3 ..... SPACE ")
        print("4 ..... VIEW ALL HOLIDAYS")
        print("5 ..... QUIT PROGRAM")
        print("="*75)
        option = input("Select: ")
        print()
        return option
    
    def quit_program():
        print("="*75)
        print("<:::> GOOD BYE <:::>")
        print("="*75)

    def invalid_entry():
        print("Invalid ENTRY!!! Please select 1,2,3,4,  and 5")

    holidays=[]

    selection=select()


    while True:
        
        if selection == "1":
            destination=input("Enter your Destination:\t\t")
            duration=input("Enter days you are going to stay for?:\t")
            resort=input("Enter your resort:\t")    
            holidays.append(Beach(destination, duration,resort))   
            print()
            print("="*50)
            print(f"<::> {holidays[-1].__class__.__name__} HOLIDAY ADDED SUCCESSFULLY <::>")  ##confirmation message
            print()
            holidays[-1].display_holiday_info()   ##Calls method to show all details
            print("="*50)

        elif selection == "2":
            destination=input("Enter your Destination:\t\t")
            duration=input("Enter days you are going to stay for?:\t")
            resort=input("Enter your resort:\t")    
            holidays.append(Ski(destination, duration,resort))   
            print()
            print("="*50)
            print(f"<::> {holidays[-1].__class__.__name__} HOLIDAY ADDED SUCCESSFULLY <::>") 
            print() 
            holidays[-1].display_holiday_info()   
            print("="*50)

        elif selection == "3":
            destination=input("Enter your Destination:\t\t")
            duration=input("Enter days you are going to stay for?:\t")
            resort=input("Enter your resort:\t")    
            holidays.append(Space(destination, duration,resort))   
            print()
            print("="*50)
            print(f"<::> {holidays[-1].__class__.__name__} HOLIDAY ADDED SUCCESSFULLY <::>") 
            print() 
            holidays[-1].display_holiday_info()   
            print("="*50)

            
        elif selection == "4":
            print("="*75)
            print("ALL HOLIDAYS")
            print("="*75)
            for holiday in holidays:
                holiday.display_holiday_info()
            print("="*75)

    
        elif selection == "5":
            quit_program()
            break

        else:
            invalid_entry()

        selection=select()
    

##Main Dispatcher
while True:
    choice = main_menu()
    if choice == "1":
        sports_program()
    elif choice == "2":
        holiday_program()
    elif choice == "3":
        break