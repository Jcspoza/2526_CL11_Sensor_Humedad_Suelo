# Taller Programación y Robótica en CMM BML – 2025 - 2026 - CL11 Sensor Humedad suelo
# Programa: Pruebas de lectura de sensor humadad tipo spakfun - con potenciometro
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2026 03
# Licencia : CC BY-NC-SA 4.0
# REf basica 
# 1.0 -> 1.1 CALIBRACION FINA

from machine import ADC
from time import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External potenciometer on GPIO26 ADC0 - pata + a VCC"
p_project = "Potenciometer basic reading with ADC0"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end


# 1- Crea el objeto ADC que conecta el pin central
# del potenciometro a adc0 = gpio 26
# Los otros 2 pines a +3.3 y 0 volt respectivamente

POTENCIOMETRO_ADC = 0 # es el ADC0
potentiometer = machine.ADC(POTENCIOMETRO_ADC)
MAXVOLT = 3.30
MINVOLT = 0.0002
MAXU16 = 65535
MINU16 = 64
FACTOR_CONVERSION = (MAXVOLT - MINVOLT) / (MAXU16 - MINU16)

# 2- Bucle de lectura
while True:
    potvalueRaw = potentiometer.read_u16()
    voltios = MINVOLT + (potvalueRaw - MINU16) * FACTOR_CONVERSION
    print(f"Voltaje leido = {voltios:.3f} voltios | Valor ADC bruto = {potvalueRaw}")
    # print(f"Voltaje leido = {voltios:.2f} voltios")
    sleep(.5)
    
