# 2526CL11_Sensor_Humedad_de_suelo

Estudio del sensor de Humedad de suelo tipo sparkfun / el del kit Kepler de sunfounder

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

---

## Proyecto completo-> en inicio de pruebas : sensor humedad suelo + bomba agua (motor)

Esta lección forma parte del los aprendizajes necesarios para controlar cargas analógicas de cierta potencia como un motor

## Clase11 - Indice

- Resumen inicial
  
  - Tópicos que se van a aprender
  
  - Lista de materiales
  
  - Links a Tutoriales e informacion
  
  - Librerías usadas
  
  - Tabla resumen de programas

- Panorama de Sensores de humedad de suelo

- Estudio para **calibración** del sensor de humedad de suelo tipo Sparkfun
  
  - M#0- ADC con potenciómetro - básico

- 

- TO DO y Notas
  
  ---

## Resumen inicial

### Tópicos que se van a aprender / repasar

| Topico                     | Detalle                                                                                                                 | Links |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----- |
| Sensores humedad suelo     |                                                                                                                         |       |
| Transistores BJC en activa |                                                                                                                         |       |
| Libreria writer            | Permite para usar tipos y tamaños de letra en displays B/N, que normalmente solo usan el tipo basico de framebuffer 8x8 |       |
| Excepciones                |                                                                                                                         |       |

### Lista de Materiales

| Material                                                                                                        | Descripcion                                                                                                                                                      | Kit SF                       | Montaje |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------- |
| [Protoboard 700](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_breadboard.html) | Placa para prototipos ver apartado [Uso de la protoboard](https://github.com/Jcspoza/2526CL1_R_CircElect0#uso-de-la-protoboard). Mejor usar la protoboard de 700 | SI                           | Todos   |
| [Cables dupond M-M](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_wire.html)    | Sirven para hacer conexiones en protoboard                                                                                                                       | SI                           | Todos   |
| Pico _, 2, W, 2W                                                                                                | Vale cualquiera de los 4 modelos de Pico                                                                                                                         | SI                           | Todos   |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
|                                                                                                                 |                                                                                                                                                                  |                              |         |
| Display SH1106 + R. encoder  pulsadores                                                                         |                                                                                                                                                                  | No , pero comprado por todos | Mon#    |

### Links a informacion

| Tema | Link |
| ---- | ---- |
|      |      |
|      |      |

### Librerías usadas

| Libreria | Uso para                                                                                                     | Link |
| -------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| writer   | Permite el uso de varios tipos y tamaños de letra en displays b/n, como el ssd1306 y el SH1106 ( el nuestro) |      |
|          |                                                                                                              |      |

### Tabla resumen de programas

Todos los programas en microPython

| Programa                                                 | Montaje | HW si Robotica y Notas                                         | Objetivo de Aprendizaje |
| -------------------------------------------------------- | ------- | -------------------------------------------------------------- | ----------------------- |
| [R2526CL11_ADC_poten_1_0.py](R2526CL11_ADC_poten_1_0.py) | M#0     | potenciómetro pin central en ADC0, otros 2 pines +3.3v y 0volt | Recordar lectura ADC    |
| [R2526CL11_ADC_poten_1_1.py](R2526CL11_ADC_poten_1_1.py) | M#0     | idem + formula mapeo mas precisa                               |                         |
|                                                          |         |                                                                |                         |
|                                                          |         |                                                                |                         |
|                                                          |         |                                                                |                         |
|                                                          |         |                                                                |                         |

---

## Panorama de Sensores de humedad de suelo

Hay 2 tipòs de sensores de humedad :

1. **Resistivos**: a su vez hay 2 circuitos tipicos
   
   1. Alrededor del LM393 : Módulo YL-69 Sensor +  HC-38 Módulo => Es el mas antiguo
      
      Un [link de compra en amazon]([Fasizi 5pcs Higrómetro del Suelo Detección de Humedad Sensor de Agua Módulo YL-69 Sensor y HC-38 Módulo para Arduino : Amazon.es: Industria, empresas y ciencia](https://www.amazon.es/dp/B09Z2HJF4V/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B09Z2HJF4V&pd_rd_w=UzWmP&content-id=amzn1.sym.dec61eec-c10c-476f-b9d1-109d380c1864&pf_rd_p=dec61eec-c10c-476f-b9d1-109d380c1864&pf_rd_r=YGYD5VBSTH78PR8CEMRS&pd_rd_wg=7qsoo&pd_rd_r=859dee20-c224-4ec9-8ec8-a0cf1ca4d9e2&aref=ADW3Pdfk5q&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy))

2. **Tipo sparkfun ( alrededor de transitor BJC NPN ): es nuestro modelo**
   
   [Link de compra en aliexpres](https://es.aliexpress.com/item/1005005988953058.html?spm=a2g0o.order_list.order_list_main.17.6591194dkoeSPU&tblci=GiAkTEfW-p2qKzCddKegd0fbpqNz46nX0zj1tz5ToRqMNCDA9m4oue-eivLt8dxjMJT3UA&gatewayAdapt=glo2esp)
   
   Tutorial de sparkfun [Soil Moisture Sensor Hookup Guide - SparkFun Learn](https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide)
   
   El modulo que viene en le kit de SF es ligeramente distinto ver [2.14 Feel the Water Level &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_water.html#py-water)
   
   AUNQUE COMPARTEN EL MISMO CIRCUITO DE TRANSISTOR BJC NPN EN ACTIVA.  lo que va a variar son los valores de calibración, porque el transistor esta polarizado con diferentes valores de resistencia

3. **Capacitivos**: ver informacion en [Capacitive Soil Moisture Module &mdash; SunFounder Universal Maker Sensor Kit documentation](https://docs.sunfounder.com/projects/umsk/en/latest/01_components_basic/02-component_soil.html)
   
   Un link para comprar : [sensor capacitivo de humedad de suelo](https://es.aliexpress.com/item/1005008718136691.html?src=google&src=google&albch=shopping&acnt=439-079-4345&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=es1005008718136691&ds_e_product_merchant_id=5559803011&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21840696692&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=21844625911&gbraid=0AAAAACbpfvaNt_TGO68ir9mWggKyoDYUQ&gclid=CjwKCAjwnN3OBhA8EiwAfpTYei8uE-kjt55ke0PO_1N8Wz6YEMo2MLlAH8XYD22mlXnC8AFMWcrvzRoCviYQAvD_BwE) => son los mas modernos 

---

## Estudio para **calibración** del sensor de humedad de suelo tipo Sparkfun

### M#0 - Recordar lectura de un potenciómetro en ADC 0 ( ver 2526 CL6)

Lo primero es recordar la lectura de señales analógicas visto en [2526 CL6 Entradas_Analogicas 1er]([GitHub - Jcspoza/2526_CL6_Entradas_Analogicas1er: Clase 6- Entradas Analogicas 1er Estudio · GitHub](https://github.com/Jcspoza/2526_CL6_Entradas_Analogicas1er))

Repetimos el montaje con potenciómetro en ADC 0 o GPIO26

CONEXIONES :

    pin central del potenciómetro a adc0 = gpio 26

    los otros 2 pines del potenciómetro a +3.3 y 0 volt respectivamente => **en los siguiente montajes cambiaremos esto**

#### <u>Programas M#0</u>

[R2526CL11_ADC_poten_1_0.py](R2526CL11_ADC_poten_1_0.py)

Tanto el programa, como el montaje HW son básico. Nos interesa ver la conversión de los valores leídos en 16 bis a voltaje **y medir con el polímetro que el voltaje es correcto**



[R2526CL11_ADC_poten_1_1.py](R2526CL11_ADC_poten_1_1.py)

La version 1.1 usa un a formula de conversión mas precisa , solo por conocer como se "mapean" valores. NO la usaremos porque no necesitamos tanta precision

### M#1 - Potenciómetro en ADC0 cambiando pin 3,3volt a GPIO

Siguiendo la recomendación de la guia de Sparkfun 

[Soil Moisture Sensor Hookup Guide - SparkFun Learn](https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide)

NO vamos a alimentar el sensor de humedad de forma continua, para evitar corrosión:

"You need to supply power to VCC and GND. We recommend not powering the sensor constantly to prevent corrosion of the probes (more on this in a bit). SIG provides an analog signal out that can be attached to the ADC pin on any microcontroller. The value read on SIG will vary depending on the voltage with which you power the sensor."

Vamos a simular este montaje primero con un potenciómetro, donde uno de los pines extremos lo conectaremos a un GPIO en vez de a 3,3 volt. cunado queramso leer el sensor popndreomos a High el pin que 'alimenta' el potenciometro. Usaremso el GPIO21 por cercania

#### <u>Programa M#1</u>

De nuevo tanto el programa, como el montaje HW con potenciometro son básico, solo queremos ver si lee sin problemas 

Si quisiéramos ver que la conversión es correcta con un polímetro hay que ampliar el tiempo en high 

---

### 

## TO DO y Notas
