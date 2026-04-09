# Taller Programación y Robótica en CMM BML – 2025 - 2026 - CL11 Sensor Humedad suelo
# Programa: Pruebas de lectura de sensor humadad tipo spakfun - con potenciometro +
# Display SH1106
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2026 03
# Licencia : CC BY-NC-SA 4.0
# REf basica https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_water.html
# 1.0 -> 2.0 mas velocidad lectura, print en misma linea
# 2.0 -> 3.0 se vel voltaje en display SH1106
# 3.0 -> 3.3 mejoras area visualiza

from machine import Pin, ADC, I2C
from time import sleep
import sh1106

from os import uname
# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External pot. on ADC0 - pata + a GPIO21 + displ SH1106 gpio4&5"
p_project = "Potenciometer basic reading with ADC0 -> display"
p_version = "3.3"
p_library = "SH1106  @robert-hh"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")
# Informative block - end

# 0.0 - Constates y varaibles globales para display
WIDTH =128 
HEIGHT= 64
WIDTH_VA = 33
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# 0.1 crea bus I2C - usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

# 0.2 Creacion del objeto display
display = sh1106.SH1106_I2C(WIDTH,
                            HEIGHT,
                            i2c,
                            res = None,
                            addr = 0x3c,
                            rotate = 0) # valores 0, 90, 180, 270
display.sleep(False)
ToplineStr = f"Lee PotVg-v{p_version}"
display.fill(0)
display.text(ToplineStr, 0, 0, 1)
display.hline(0,9,128,1)
display.show()

# 1- Crea el objeto ADC que conecta el pin central
# del potenciometro a adc0 = gpio 26
# Los otros 2 pines a +3.3 y 0 volt respectivamente

POTENCIOMETRO_ADC = 0 # es el ADC0
potentiometer = machine.ADC(POTENCIOMETRO_ADC)
alimentaSensor = machine.Pin(21, machine.Pin.OUT)
MAXVOLT = 3.05
FACTOR_CONVERSION = MAXVOLT / (65535)
ESPERA = 0.5

# 2- Bucle de lectura
try:
    while True:
        alimentaSensor.on()
        potvalueRaw = potentiometer.read_u16()
        alimentaSensor.off()
        voltios = potvalueRaw * FACTOR_CONVERSION
        print(f"Voltaje leido = {voltios:.2f} voltios | Valor ADC bruto = {potvalueRaw}",end='\r')
        display.text('Leer volts Pot', 0, 11, 1)
        # ancho area de visualiza lectura 20 a 53 = 33
        voltstr = f" {voltios:.2f} voltios"
        display.text(voltstr, 0, 20, 1)
        display.show()
        sleep(ESPERA)
        display.fill_rect(0, 20,WIDTH, WIDTH_VA , 0)
        display.show() 
                
except KeyboardInterrupt:
    alimentaSensor.off()
    print("\nParada de usuario")
    display.fill(0)
    display.text(ToplineStr, 0, 0, 1)
    display.hline(0,9,128,1)
    display.hline(0,54,128,1)
    display.text('Parada x usuario', 0, 56, 1)
    display.show()
    
