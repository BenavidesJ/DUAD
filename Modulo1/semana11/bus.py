class Person():
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Bus():
    max_passengers = 5
    passenger_qty = 0
    passenger_list = []
    
        
    def add_passenger(self, passenger):
        if self.passenger_qty >= self.max_passengers:
            print(f"Passenger {passenger.name} can't go on board. The bus is full")
        else:    
            self.passenger_list.append(passenger)
            self.passenger_qty += 1
            print(f"Passenger {passenger.name} is on board, current passenger's quantity {self.passenger_qty}")
        
        
    def remove_passenger(self, passenger):
        try:
            if self.passenger_qty >= 0:
                self.passenger_list.remove(passenger)
                print(f"Passenger {passenger.name} is getting off")
                self.passenger_qty -= 1
            else:
                print(f"No one is onboard, bus is empty!")
        except:
            print(f"Passenger {passenger.name} isn't on board in this ride.")
        
    def to_string(self):
        print(f"""
                Max passengers: {self.max_passengers}
                Current passengers: {self.passenger_qty}
              """)

passenger_1 = Person("Jose")
passenger_2 = Person("Carlos")
passenger_3 = Person("Maria")
passenger_4 = Person("Laura")
passenger_5 = Person("Marcos")
passenger_6 = Person("Olga")

ride_1 = Bus()
ride_1.add_passenger(passenger_1)
ride_1.add_passenger(passenger_2)
ride_1.add_passenger(passenger_3)
ride_1.add_passenger(passenger_4)
ride_1.add_passenger(passenger_5)
ride_1.add_passenger(passenger_6)
ride_1.to_string()
ride_1.remove_passenger(passenger_5)
ride_1.remove_passenger(passenger_4)
ride_1.to_string()
ride_1.add_passenger(passenger_6)
ride_1.to_string()
ride_1.remove_passenger(passenger_6)
ride_1.remove_passenger(passenger_1)
ride_1.remove_passenger(passenger_2)
ride_1.remove_passenger(passenger_3)
ride_1.remove_passenger(passenger_5)
ride_1.to_string()
