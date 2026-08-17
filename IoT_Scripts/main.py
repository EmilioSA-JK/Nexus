#This script was created for the light, motion detector and the siren which will be activated in case the motion detector detects any movement. The light will be turned on and the siren will be activated.

from time import *
from gpio import *




def main():
	# The initial mode of the pins is defined
	pinMode(0, OUT)
	pinMode(2, IN)
	
	# Here we create a loop lo check the state of the button
	while True:
		if digitalRead(2) == HIGH:
			customWrite(0, '1')
			
		else:
			customWrite(0, '0')
			

	# The main function is called
if __name__ == "__main__":	
	main()


