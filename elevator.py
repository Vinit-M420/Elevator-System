from building import Building 
import random
import time

class Elevator:
    def __init__(self, max_floors):
       self.current_position = random.randint(0,Building.num_floors-1)
       self.max_floors = Building.num_floors
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
        for floor in range(self.current_floor,called_floor-1,-1):
            if floor == 0:
                print('Elevator position: GND')
            elif floor == called_floor:
                print(f'Elevator reached: {floor}')    
            else:
                print(f'Elevator position: {floor} ↧↧')
            time.sleep(self.time_limit)                
            self.current_floor = floor                
                
    def callingElevator(self, floor):
        if floor > 0:
            print(f'The button is pressed: {floor} Floor')
        else:
            print('The button is pressed: GND Floor')
            
        callingSensor = random.choice([True, False])
    
        if callingSensor == True and self.current_position == floor:
            print(f"The elevator isn't moving. The elevator is already at {floor} floor")
        elif callingSensor:
            print(f'A person is detected. The elevator is moving towards Floor {floor}')
            if floor > self.current_position:
                self.move_up(floor)
            else:
                self.move_down(floor)             
        else:
            print(f'No person is detected. The elevator is remaining idle.')    
            
    
    def get_current_position(self):
        if self.current_position == 0:
            print("The Elevator position : GND floor")
        else:
            print(f"The Elevator position : Floor {self.current_position}")
        return self.current_position                          
                