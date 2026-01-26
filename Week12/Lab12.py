class suspect:
       #init. method
    def  __init__(self,title,name,location):

        self.title = title
        self.name = name
        self.location = location

#define methods 
    def who_are_you(self):   
        print(f"I am {self.title:10} {self.name:10}")    #I am Miss Scarlet
        print("_"*50)
    def where_are_you(self):            
        print(f"{self.title:10} {self.name:10}is in the  {self.location:10}")  #Rev Green is in the Hall
        print("_"*50)
#create 3 objects->>characters and locations  from Cluedo
player1 = suspect("Professor","Plum","Kitchen")
player2 = suspect("Mrs.","White","Lounge")
player3 = suspect("Mr.","Body","Ballroom")

#call the who_are_you method for each object
player1.who_are_you()
player2.who_are_you()
player3.who_are_you()

#call the where_are_you method for each object
player1.where_are_you()
player2.where_are_you()
player3.where_are_you()

