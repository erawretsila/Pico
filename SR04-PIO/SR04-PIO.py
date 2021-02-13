import time
import rp2 
from rp2 import PIO, asm_pio
from machine import Pin

@asm_pio(set_init=(PIO.IN_LOW),sideset_init=PIO.OUT_LOW)
def SR04():
    wait(0,pin,0)              #check echo pin is low before starting
    mov(x,null) .side(1)[7]    #set trigger pin high & clear x register
    mov(y,null) .side(0)             #return trigger to low
    label ('wait')              #wait for start of echo pulse
    jmp (pin,'countdown')       #start timing when pin goes high
    jmp (y_dec,'wait')          #loop arround untill count expires
    jmp ('exit')                #exit
    label('countdown')
    jmp(x_dec,'skip')          #decrement x reg
    label('skip')             
    jmp(x,'exit')              #exit if x 0 #time out
    jmp(pin,'countdown')       #ping still high continue counting
    label ('exit')
    mov(isr, invert(x))        #invert x & prepare to output
    push()                     #output to Fifo
    
#example usage    
sm=rp2.StateMachine(1,SR04,freq=500000,set_base=Pin(0),sideset_base=Pin(1))
sm.active(1)

while True:
    print(sm.get())
    time.sleep(.1)
 
