import time
import rp2 
from rp2 import PIO, asm_pio
from machine import Pin

@asm_pio(set_init=(PIO.IN_LOW),sideset_init=PIO.OUT_LOW)
def SR04():
    label ('start')
    wait(0,pin,0)              #check echo pin is low before starting
    mov(x,null) .side(1)[7]    #set trigger pin high & clear x register
    nop() .side(0)             #return trigger to low
    wait(1,pin,0)              #wait for start of echo pulse
    label('countdown')
    jmp(x_dec,'skip')          #decrement x reg
    label('skip')             
    jmp(x,'exit')              #exit if x 0 #time out
    jmp(pin,'countdown')       #ping still high continue counting
    mov(isr, invert(x))        #invert x & prepare to output
    push()                     #output to Fifo
    label ('exit')
    jmp ('start')              #echo has timed out, return to start.
    
#example usage    
sm=rp2.StateMachine(1,SR04,freq=500000,set_base=Pin(0),sideset_base=Pin(1))
sm.active(1)

while True:
    print(sm.get())
    time.sleep(.1)
