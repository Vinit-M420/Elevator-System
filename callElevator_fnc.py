import random 

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
            
callingElevator()
                