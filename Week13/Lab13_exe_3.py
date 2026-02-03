##EXERCISE 3

class Cube:
    def __init__(self,side):
        self.side=side

    def calculate_volume(self):
        return self.side **3
    
class Cuboid: 
    def __init__(self,length,width,height):
       self.length=length
       self.width=width
       self.height=height
    
    def calculate_volume(self):
       
       return self.length*self.width*self.height

class Sphere:  
    def __init__(self,radius):
        self.radius=radius
            
    def calculate_volume(self):

        return (4/3)*3.14*(self.radius**3)
  
class TriangularPrism:  
    def __init__(self,base,height,length):
        self.base=base
        self.height=height
        self.length=length
        
    def calculate_volume(self):
        
        return 0.5*(self.base*self.height*self.length)
    
  
##Main Menu

def select():    
    print()
    print("="*75)
    print("GEOMETRIC VOLUMES")
    print("="*75)
    print("1 ..... CUBE")
    print("2 ..... CUBOID")
    print("3 ..... SPHERE")
    print("4 ..... TRIANGULAR PRISM")
    print("5 ..... VIEW VOLUMES")
    print("6 ..... QUIT PROGRAM")
    print("="*75)
    option=input("Select :")
    print()
    return option 

def quit_program():
    print("="*75)
    print("GOODBYE...")
    print("="*75)

def invalid_entry():
    print("Invalid! Please select option 1,2,3,4,5 or 6")   

       

volumes = []

 
selection=select()

###Main program

while True:
    if selection=="1":
        side = float(input("Enter Side=\t"))
        volumes.append(Cube(side))
        print()
        print("="*50)
        print(f"{volumes[-1].__class__.__name__:10}Volume= {volumes[-1].calculate_volume():5}")     ###[-1] is for last item added to list 
        print("="*50)
    elif selection=="2":
        length= float(input("Enter length=\t"))
        width= float(input("Enter width=\t"))
        height= float(input("Enter height=\t"))
        volumes.append(Cuboid(length,width,height))
        print()
        print("="*50)
        print(f"{volumes[-1].__class__.__name__:10}Volume= {volumes[-1].calculate_volume():5}")
        print("="*50)

    elif selection=="3":
        radius= float(input("Enter radius=\t"))
        volumes.append(Sphere(radius))
        print()
        print("="*50)
        print(f"{volumes[-1].__class__.__name__:10}Volume= {volumes[-1].calculate_volume():5}")
        print("="*50)
    elif selection=="4":
        base= float(input("Enter base=\t"))
        height= float(input("Enter height=\t"))
        length= float(input("Enter length=\t"))
        volumes.append(TriangularPrism(base,height,length))
        print()
        print("="*50)
        print(f"{volumes[-1].__class__.__name__:10}Volume= {volumes[-1].calculate_volume():5}")
        print("="*50)
    
    elif selection=="5":
        for volume in volumes:
            print(f"{volume.__class__.__name__:18}Volume= {volume.calculate_volume():5}")
            
    
    elif selection=="6":
        
        quit_program()
        break  
    else:
        invalid_entry()
    
    selection=select()


    