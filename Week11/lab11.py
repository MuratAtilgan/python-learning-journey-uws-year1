## Monty Python -"The Pythons":) 

class student:

    #init. method

    def __init__(self,first_name,surname,university,course):
        self.first_name = first_name
        self.university =university
        self.surname = surname
        self.course = course
    
    #define method

    def list_of_Monty_Python(self):
        print(f"{self.first_name:10} {self.surname:10}study    {self.course:20}  at   {self.university:10}")


#create 6 instances(objects) -6 member of Monty Python

student1 = student("Graham","Chapman","UWS","BSc Computer Science")
student2 = student("John","Cleese","UWS","BSc Law")
student3 = student("Terry","Gilliam","UWS","BSc Mathematics")
student4 = student("Eric","Idle","UWS","BSc Cyber Security")
student5 = student("Terry","Jones","UWS","BSc Finance")
student6 = student("Michael","Palin","UWS","BSc Art")

#call the list_of_Monty_Python

student1.list_of_Monty_Python()
student2.list_of_Monty_Python()
student3.list_of_Monty_Python()
student4.list_of_Monty_Python()
student5.list_of_Monty_Python()

student6.list_of_Monty_Python()
