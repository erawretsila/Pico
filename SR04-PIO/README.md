SR04 Readme


udated code
there are now 2 versions of code

SR04Pio1
This version requires manual trigering for each ping/echo
usefull if more than 1 SR04 is in use

SR0rPi02
This version is free runnig generating an interupt each time a result is redy for recieving
provided a suitable interup handler is available there should be no lag on readings due to the FIFO buffer filling 
if no IRQ handler then the srevice will stall when the bufer is full & the readings may not be current

in either instance if there is an error with the sensor the code will time out & return 0

the Pio files should be ok but have not yet been tested

