#Single ELevator Single Request

import random
import time

floors = input('Please enter the number of floors in the building:')
time_limit = 3
try:
    floors = int(floors)
    if floors <= 0:
        print('Number of floors of a building must be atleast 1. Defaulting 8')
        floors = 8
except ValueError:
    print('Invalid Input. Defaulting 8 floors')          # default number of floors
    floors = 8
    
current_position = random.randint(0,floors-1)
def buildingSize():
    print(f"The building has {floors} floors.")     
      
buildingSize()
   
def position():                                          # Elevator's position
    if current_position == 0:
           print("The Elevator position : GND floor")
    else:    
           print(f"The Elevator position : Floor {current_position}")
    return current_position   
           
           
position()
print(f'Current position of the elevator: {current_position}')
           

def callingElevator(floor):
    global callingSensor                                # Declaring  as global
    if floor > 0:
        print(f'The button is pressed: {floor} Floor')
    else:
        print('The button is pressed: GND Floor')             
    
    callingSensor = random.choice([True, False])
    
    if callingSensor == True and current_position == floor:
        print(f"The elevator isn't moving. The elevator is already at {floor} floor")
    elif callingSensor:
        print(f'A person is detected. The elevator is moving towards Floor {floor}')        
    else:
        print(f'No person is detected. The elevator is remaining idle.')   


# Simulate calling the elevator
called_floor = random.randint(0, floors)
if called_floor == 0:
    print("The elevator is called to GND floor.")   
else:
    print(f"Simulating button press at: Floor {called_floor}")

callingElevator(called_floor) 
        
print(" ") 
print(f'Current position of the elevator: {current_position}')

       
def elevatorMovement():
    global current_position
    position1 = current_position
    if callingSensor == False:
        exit
    else:    
        if called_floor > position1:
            for pos in range(position1,called_floor+1):
                if pos == 0:
                    print(f'Elevator position: GND ↥↥')
                    time.sleep(time_limit) 
                elif pos == called_floor:
                    print(f'Elevator reached: {pos}')       
                else:    
                    print(f'Elevator position: {pos} ↥↥')
                    time.sleep(time_limit) 
                position1 = pos           
        elif called_floor < position1:
            for pos in range(position1,called_floor-1,-1):
                if pos == 0:
                    print('Elevator position: GND')
                elif pos == called_floor:
                    print(f'Elevator reached: {pos}')    
                else:
                    print(f'Elevator position: {pos} ↧↧')
                    time.sleep(time_limit)                
                position1 = pos
        elif position1 == called_floor:
            exit        
        else:
            print(f'Elevator reached: {position1}')
        
        current_position = position1    
                             
elevatorMovement()                    

#print(f'Current position of the elevator: {current_position}')            
           