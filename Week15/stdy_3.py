import random

class People:
    
    def __init__(self,person_name):
        self.person_name=person_name
        self.pet=Pet()
        self.vehicle=Car()
        self.living=House()
        

    
    def display(self):
        print()
        print("="*65)
        print()
        print(f"Person:\t\t{self.person_name} live at {self.get_address()}")
        print()
        print(f"Pet:\t\tHas a {self.pet.get_pet()} and its name is {self.pet.get_pet_name()}")
        print()
        print(f"Car:\t\tOwn a {self.vehicle.get_car_colour()} colour {self.vehicle.get_car()}")
        print()
        print(f"Property:\tOwns a {self.living.get_house()}")
        print()
        print("="*65)
        print()
        print("LOVE ANIMALS")
        print()


class Personal_Details(People):

    def __init__(self, person_name):
        super().__init__(person_name) 
        

        addresses=["1  Orsay Cresscent, Glasgow,G13 5FG","6A Yellow Avenue, Glasgow,G23 7ER","14 Brown street,Hamilton, ML1 7TH","77 Green court, Motherwell,ML3 5DF"]

        self.per_address=random.choice(addresses)

    def get_address(self):
        
        return self.per_address
    

            
class Pet:

    def __init__(self):
         pets=["Cat","Parrot","Dog","Lion"]

         pet_names=["Murphy","Oscar","Talent","Pisagor"]
         
         self.pet_kind=random.choice(pets)
         self.pet_name=random.choice(pet_names)

    def get_pet(self):
        
        return self.pet_kind
    
    def get_pet_name(self):
        return self.pet_name
    
    

class Car:

    def __init__(self):
        
        vehicles=["Rolls Royce","Renault Megane","Lada Samara","Maybach"]

        colours=["Black","Green","Red","White"]

        self.veh_typ=random.choice(vehicles)
        self.veh_clr=random.choice(colours)

    def get_car(self):

        return self.veh_typ
    
    def get_car_colour(self):

        return self.veh_clr
        
    

    
class House:

    def __init__(self):
        
        properties=["Flat","Villa","Bungalow","Detached"]

        self.living=random.choice(properties)
        
        

    def get_house(self):

        return self.living

   

p1=Personal_Details("Muratti")
p2=Personal_Details("Jordan")
p3=Personal_Details("Shaun")
p4=Personal_Details("Joann")

p1.display()
p2.display()
p3.display()
p4.display()



