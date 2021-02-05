SR04 Readme

This PIO code will repeatedly ping an SR04 sensor & place the echo time
into the FIFO for reading as a 32 bit count

running the State machine at 500khz gives an output integer that is
approximately scaled to approxinaty  1mm acurate enough for most
robotics projects which only need rough near/far indicators
 
if run at faster speeds or where acurate readings are essential 
(digital tape measure) a scaling factor will need to be 
applied & calibrated
