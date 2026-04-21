# Hardware platform: Pico W & Pico + Display SH1106 + REncoder + 3 switch
# Author : JC Santamaria 
# Date : 2025 - 2 - 20
# Goal : External switch in GPIO18 with interrups , count pressed & debounce
# Learning Target : interruptions basic
# Ref : 

from machine import Pin # Get the Pin function from the machine module.
import utime  

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO18 IN (pull up externally)"
p_project = "Switch with interruption with loop"
p_version = "3.0 debounce 200ms"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

CONFIRM = 18
BACK = 19
PUSH = 20
pulsador = Pin(PUSH, Pin.IN)

intled = Pin("LED", Pin.OUT)
intled.on()

veces_pulsadas = 0 # guarda las veces que se presiono el pulsador
last_time = 0 # guarda la ultima marca de tiempo en que se presiono el pulsador

def manejaPulsador(pin):    
    global veces_pulsadas, last_time
    new_time = utime.ticks_ms()
    # Si ha pasado mas de 200ms desde el ultimo evento, temenos un nuevo evento. Evita los REBOTES
    if utime.ticks_diff(new_time, last_time) > 100: 
        veces_pulsadas += 1
        print(int(str(pin).split(",")[0][8:]))
        last_time = new_time
        
pulsador.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsador)

intled = Pin("LED", Pin.OUT)
intled.on()

veces_pulsadas_viejo = 0
while True:
    print('hago cosas y hago parpadear el led')
    utime.sleep(1)
    if veces_pulsadas_viejo != veces_pulsadas:
       print('Veces pulsadas = ', veces_pulsadas)
       veces_pulsadas_viejo = veces_pulsadas
       
    intled.toggle() # cambia el led de encendido a apagado y viceversa

