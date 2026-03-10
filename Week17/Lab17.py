class flight:

    def __init__(self,flight_number,airline,leaving_from,going_to):

        self.flight_number=flight_number
        self.airline=airline
        self.leaving_from=leaving_from
        self.going_to=going_to

flight1=flight("FR5771","Ryan Air","Glasgow","Dublin")
flight2=flight("KL1473","KLM","Amsterdam","Glasgow")
flight3=flight("EK023","Emirates","Dubai","Edinburgh")
flight4=flight("EZY6907","EasyJet","Edinburgh","Geneva")
flight5=flight("SQ24","Singapore","Newyork","Singapore")
flight6=flight("QF8045","Qantas","Sidney","Frankfurt")

flights={flight1.flight_number:flight1,flight2.flight_number:flight2,flight3.flight_number:flight3,flight4.flight_number:flight4,flight5.flight_number:flight5,flight6.flight_number:flight6}

print()

flight_number=input("Enter your flight number or Q to quit>>").strip().upper()

print()

while flight_number != "Q":

    if flight_number in flights.keys():
        flight_info=flights[flight_number]
        print()
        print()
        print(f"Your flight details\t>>> Flight number: {flight_info.flight_number} from {flight_info.leaving_from} to {flight_info.going_to} by {flight_info.airline} Airlines")
        print()
        print()
    
    else:
        print()
        print("Flight not found")
        print()
    flight_number=input("Enter another flight number or Q for quit>>").strip().upper()
    print()

print("Good Bye")
print()


