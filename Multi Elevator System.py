## Multi Elevator System
import random
import time

class Building:
    def __init__(self, num_floors,num_elevator):
        self.num_floors = num_floors
        self.num_elevator = num_elevator
        self.elevators = [Elevator(self, elevator_id =i+1) for i in range(num_elevator)]
        
    def buildingSize(self):
        print(f"The building has {self.num_floors} floors and {self.num_elevator} elevator.")
        
        
    def assign_requests(self,floor_requests):
        closest_elevator = 0
        min_distance = float('inf')
        
        for elevator in self.elevators:
            distance = abs(elevator.current_position - floor_requests)
            if distance < min_distance:
                min_distance = distance
                closest_elevator = elevator  
        
        print(f"Assigning request for floor {floor_requests} to Elevator {closest_elevator.elevator_id}")
        return closest_elevator    

class Elevator:
    def __init__(self, building, elevator_id):
       self.building = building
       self.elevator_id = elevator_id
       self.current_position = random.randint(0,building.num_floors-1)
       #self.current_position2 = random.randint(0,building.num_floors-1)
       self.time_limit = 3
    
    def move_up(self, called_floor):
        for floor in range(self.current_position,called_floor+1):
            if floor == 0:
                print(f'Elevator {self.elevator_id} position: GND ↥↥') 
            elif floor == called_floor:
                print(f'Elevator {self.elevator_id} reached: {floor}')       
            else:    
                print(f'Elevator {self.elevator_id} position: {floor} ↥↥')
            time.sleep(self.time_limit) 
            self.current_position = floor
    
    def move_down(self, called_floor):
        for floor in range(self.current_position,called_floor-1,-1):
            if floor == 0:
                print(f'Elevator {self.elevator_id} position: GND')
            elif floor == called_floor:
                print(f'Elevator {self.elevator_id} reached: {floor}')    
            else:
                print(f'Elevator {self.elevator_id} position: {floor} ↧↧')
            time.sleep(self.time_limit)                
            self.current_position = floor                
                
             
    # def callingElevators(self,floor_requests):
    #     print('All requests are stimulating')
        
    #     up_requests = sorted([floor for floor in floor_requests if floor >= self.current_position and floor <= self.building.num_floors])
    #     down_requests = sorted([floor for floor in floor_requests if 0 <= floor < self.current_position], reverse = True)
        
        
    #     for floor in up_requests+down_requests:
    #         #print(down_requests)
    #         if floor == self.current_position:
    #             print(f"The elevator isn't moving. The elevator is already at {floor} floor")
    #         elif floor > self.current_position:
    #             self.move_up(floor)
    #             floor = self.current_position
    #         else:
    #             self.move_down(floor)
    #         #floor = self.current_position 
    #     print('All requests processed')   
                 
              
    def get_current_position(self):
        if self.current_position == 0:
            print(f"The Elevator {self.elevator_id} position : GND floor")
        else:
            print(f"The Elevator {self.elevator_id} position : Floor {self.current_position}")
        
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
    
my_building = Building(floors,2)
my_building.buildingSize()    

my_elevator = Elevator(my_building, elevator_id=1)       # Pass the building instance to the Elevator instance

for elevator in my_building.elevators:
    elevator.get_current_position()

floor_requests = [5,6,2,10]
floor_requests = [floor for floor in floor_requests if floor <=floors]
print(floor_requests)
for request in floor_requests:
    closest_elevator = my_building.assign_requests(request)
    
    print(f"Closest elevator to floor {request} is Elevator {closest_elevator.elevator_id}")
    if request < closest_elevator.current_position:
        closest_elevator.move_down(request)
    elif request > closest_elevator.current_position:
        closest_elevator.move_up(request)    
