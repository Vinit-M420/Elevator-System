#Single Elevator Multiple Requests


import random
import time

class Building:
    def __init__(self, num_floors,num_elevator):
        self.num_floors = num_floors
        self.num_elevator = 1
        
    def buildingSize(self):
        print(f"The building has {self.num_floors} floors.")   
        

class Elevator:
    def __init__(self, building):
       self.building = building
       self.current_position = random.randint(0,building.num_floors-1)
       self.current_position2 = random.randint(0,building.num_floors-1)
       self.time_limit = 3
    
    def move_up(self, called_floor):
        for floor in range(self.current_position,called_floor+1):
            if floor == 0:
                print(f'Elevator position: GND ↥↥') 
            elif floor == called_floor:
                print(f'Elevator reached: {floor}')       
            else:    
                print(f'Elevator position: {floor} ↥↥')
            time.sleep(self.time_limit) 
            self.current_position = floor
    
    def move_down(self, called_floor):
        for floor in range(self.current_position,called_floor-1,-1):
            if floor == 0:
                print('Elevator position: GND')
            elif floor == called_floor:
                print(f'Elevator reached: {floor}')    
            else:
                print(f'Elevator position: {floor} ↧↧')
            time.sleep(self.time_limit)                
            self.current_position = floor                
                
             
    def callingElevators(self,floor_requests):
        print('All requests are stimulating')
        
        up_requests = sorted([floor for floor in floor_requests if floor >= self.current_position and floor <= self.building.num_floors])
        down_requests = sorted([floor for floor in floor_requests if 0 <= floor < self.current_position], reverse = True)
        
        
        for floor in up_requests+down_requests:
            #print(down_requests)
            if floor == self.current_position:
                print(f"The elevator isn't moving. The elevator is already at {floor} floor")
            elif floor > self.current_position:
                self.move_up(floor)
                floor = self.current_position
            else:
                self.move_down(floor)
            #floor = self.current_position 
        print('All requests processed')   
                 
              
    def get_current_position(self):
        if self.current_position == 0:
            print("The Elevator position : GND floor")
        else:
            print(f"The Elevator position : Floor {self.current_position}")
        return self.current_position          


floors = input('Please enter the number of floors in the building:')
try:
    floors = int(floors)
    if floors < 1:
        print('Number of floors of a building must be atleast 1. Defaulting 8')
        floors = 8
except ValueError:
    print('Invalid Input. Defaulting 8 floors')          # default number of floors
    floors = 8
    
my_building = Building(floors,1)
my_building.buildingSize()    

my_elevator = Elevator(my_building)                     # Pass the building instance to the Elevator instance
my_elevator.get_current_position()

floor_requests = [5,6,2,8,-1]

my_elevator.callingElevators(floor_requests)