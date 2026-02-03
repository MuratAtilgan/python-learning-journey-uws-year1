##EXERCISE 1

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

class Rectangle:  #new class
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth       ####Area of a rectangle = length * breadth
    
    def calculate_area(self):

        return self.length*self.breadth
  
class Triangle:  #new class
    def __init__(self,base,height):
        self.base=base             ###Area of a triangle = 0.5 * base * height
        self.height=height
        
    def calculate_area(self):
        return 0.5*(self.base*self.height)
    

     
shapes = [Circle(7),Square(9),Rectangle(11,6),Triangle(8,4)]


for shape in shapes:
    print()
    print(f"{shape.__class__.__name__:12}  area = {shape.calculate_area()}")   ##{shape.__class__.__name__}
    print()