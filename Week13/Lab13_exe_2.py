##EXERCISE 2

class Square:
    def __init__(self,side):
        self.side=side

    def calculate_area(self):
        return self.side **2
    
class Circle: 
    def __init__(self,radius):
       self.radius=radius
    
    def calculate_area(self):
       
       return 3.14* (self.radius**2)

class Rectangle:  
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def calculate_area(self):

        return self.length*self.breadth
  
class Triangle:  
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def calculate_area(self):
        return 0.5*(self.base*self.height)
    
  
##Main Menu

def select():    
    print()
    print("="*75)
    print("GEOMETRIC SHAPES")
    print("="*75)
    print("1 ..... SQUARE")
    print("2 ..... CIRCLE")
    print("3 ..... RECTANGLE")
    print("4 ..... TRIANGLE")
    print("5 ..... VIEW AREAS")
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

       

shapes = []

 
selection=select()

###Main program

while True:
    if selection=="1":
        side = float(input("Enter Side=\t"))
        shapes.append(Square(side))
        print()
        print("="*50)
        print(f"{shapes[-1].__class__.__name__:10}Area= {shapes[-1].calculate_area():5}")     ###[-1] is for last item added to list 
        print("="*50)
    elif selection=="2":
        radius= float(input("Enter Radius=\t"))
        shapes.append(Circle(radius))
        print()
        print("="*50)
        print(f"{shapes[-1].__class__.__name__:10}Area= {shapes[-1].calculate_area():5}")
        print("="*50)

    elif selection=="3":
        length= float(input("Enter length=\t"))
        breadth= float(input("Enter breadth=\t"))
        shapes.append(Rectangle(length,breadth))
        print()
        print("="*50)
        print(f"{shapes[-1].__class__.__name__:10}Area= {shapes[-1].calculate_area():5}")
        print("="*50)
    elif selection=="4":
        base= float(input("Enter base=\t"))
        height= float(input("Enter height=\t"))
        shapes.append(Triangle(base,height))
        print()
        print("="*50)
        print(f"{shapes[-1].__class__.__name__:10}Area= {shapes[-1].calculate_area():5}")
        print("="*50)
    
    elif selection=="5":
        for shape in shapes:
            print(f"{shape.__class__.__name__:10}Area= {shape.calculate_area():5}")
            
    
    elif selection=="6":
        
        quit_program()
        break  
    else:
        invalid_entry()
    
    selection=select()


    