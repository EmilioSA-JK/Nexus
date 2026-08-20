#This script was created for the light, motion detector and the siren which will be activated in case the motion detector detects any movement. The light will be turned on and the siren will be activated.

from time import *
from gpio import *




def main():
	# The initial mode of the pins is defined
	pinMode(0, OUT)
	pinMode(2, IN)
	pinMode(3, IN)
	pinMode(1, OUT)
	# Here we create a loop to check the state of the switch continuously
	while True:
		#Here we define the conditional to check the switch status
		#Depending on the status "High" or "Low" the condition will write a state for the IoT device
		if digitalRead(2) == HIGH:
			customWrite(0, '1')
			
		else:
			customWrite(0, '0')
			
		if digitalRead(3) == HIGH:
			customWrite(1, '2')
			
		else:
			customWrite(1, '0')

	# The main function is called
if __name__ == "__main__":	
	main()