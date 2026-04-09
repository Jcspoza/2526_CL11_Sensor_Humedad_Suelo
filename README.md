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
  
  - M#1- ADC con potenciómetro - básico + formula de mapeo
  - M#2 - ADC con potenciómetro  un extremo a GPIO para evitar corrosión
  - M#3
  - M#4
  - Calibración con M#4
  - M#5 - mas autónoma ( sin PC)

- TO DO y Notas

- ---

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

Comprobar que estén en la menoría de la PICO y preferentemente en /lib. si no estan copiar los ficheros a /lib

Seguramente 'writer.py' no estará.

| Libreria                       | Uso para                                                                                                     | Link                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sh1106.py](sh1106.py)         | manejo del display b/n grafico SH1106 de 1.3 pulgadas y128 x 64 pixeles                                      | [https://github.com/robert-hh/SH1106](https://github.com/robert-hh/SH1106)                                                                         |
| [writer.py](writer.py)         | Permite el uso de varios tipos y tamaños de letra en displays b/n, como el ssd1306 y el SH1106 ( el nuestro) | [https://github.com/peterhinch/micropython-font-to-py/tree/master/writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) |
| [freesans20.py](freesans20.py) | Letra alternativa a usar con writer                                                                          |                                                                                                                                                    |
| [inkfree20.py](inkfree20.py)   | Letra alternativa a usar con writer                                                                          |                                                                                                                                                    |

### Tabla resumen de programas

Todos los programas en microPython

| Programa                                                           | Montaje | HW si Robotica y Notas                                                            | Objetivo de Aprendizaje                                                 |
| ------------------------------------------------------------------ | ------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [R2526CL11_ADC_poten_1_0.py](R2526CL11_ADC_poten_1_0.py)           | M#1     | potenciómetro pin central en ADC0, otros 2 pines +3.3v y 0volt                    | Recordar lectura ADC                                                    |
| [R2526CL11_ADC_poten_1_1.py](R2526CL11_ADC_poten_1_1.py)           | M#1     | idem + formula mapeo mas precisa                                                  |                                                                         |
| [R2526CL11_ADC_potVccgpio_2_0.py](R2526CL11_ADC_potVccgpio_2_0.py) | M#2     | potenciómetro uno de los ines extremso a GPIO21 -> evitar corrosión + excepciones | simular montaje de sensor  humedad con potenciómetro                    |
| [R2526CL11_ADC_potVccgpio_2_1.py](R2526CL11_ADC_potVccgpio_2_1.py) | M#2     | mejoras de presentación , misma linea                                             | idem                                                                    |
| [Rbhwt_sh1106_1_0.py](Rbhwt_sh1106_1_0.py)                         | M#3     | Prueba basica de HW del display SH1106                                            | requiere libreria 'sh1106.py'                                           |
| [R2526CL11_ADC_pVgDisp_3_3.py](R2526CL11_ADC_pVgDisp_3_3.py)       | M#3     | Añadir display b/n SH1106                                                         | Hacer el montaje mas autónomo ( sin pc) + requiere libreria 'sh1106.py' |
| [Rbhwt_sh1106_writer_1_0.py](Rbhwt_sh1106_writer_1_0.py)           | M#4     | prueba basica de letra grande en display SH1106                                   | requiere libreria 'sh1106.py' + 'writer.py' + una fuente de letra       |
| [R2526CL11_ADC_pVgDisp_4_0.py](R2526CL11_ADC_pVgDisp_4_0.py)       | M#4     | leer pot con Vcc en gpio21 + sh1106 + letra grande                                | requiere libreria 'sh1106.py' + 'writer.py' + una fuente de letra       |
| [R2526CL11_ADC_pVgDisp_4_1.py](R2526CL11_ADC_pVgDisp_4_1.py)       |         | idem con mejoras 1                                                                | requiere libreria 'sh1106.py' + 'writer.py' + una fuente de letra       |
| [R2526CL11_ADC_pVgDisp_4_2.py](R2526CL11_ADC_pVgDisp_4_2.py)       |         | idem con mejoras 2                                                                |                                                                         |

---

## Panorama de Sensores de humedad de suelo

Hay 2 tipos de sensores de humedad :

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

#### <u>Programas M#1</u>

[R2526CL11_ADC_poten_1_0.py](R2526CL11_ADC_poten_1_0.py)

Tanto el programa, como el montaje HW son básico. Nos interesa ver la conversión de los valores leídos en 16 bis a voltaje **y medir con el polímetro que el voltaje es correcto**

[R2526CL11_ADC_poten_1_1.py](R2526CL11_ADC_poten_1_1.py)

La version 1.1 usa un a formula de conversión mas precisa , solo por conocer como se "mapean" valores. NO la usaremos porque no necesitamos tanta precisión.

**Recordar uso de ploter en monitor de Thonny** : mejor solo una variable o si son 2 que tengan limites similares

### M#2 - ADC con potenciómetro : un extremo a GPIO para evitar corrosión

Siguiendo la recomendación de la guia de Sparkfun 

[Soil Moisture Sensor Hookup Guide - SparkFun Learn](https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide)

**NO vamos a alimentar el sensor de humedad de forma continua, para evitar corrosión:**

"You need to supply power to VCC and GND. We recommend not powering the sensor constantly to prevent corrosion of the probes (more on this in a bit). SIG provides an analog signal out that can be attached to the ADC pin on any microcontroller. The value read on SIG will vary depending on the voltage with which you power the sensor."

Vamos a simular este montaje primero con un potenciómetro, donde uno de los pines extremos lo conectaremos a un GPIO en vez de a 3,3 volt. cunado queramso leer el sensor popndreomos a High el pin que 'alimenta' el potenciómetro. Usaremos el GPIO21 por cercania

#### <u>Programas M#2</u>

El montaje HW con potenciómetro es básico, pero en el programa usaremos una **excepción** para salir del bucle por teclado. pero de nuevo, solo queremos ver si lee sin problemas 

Conversion : usamso la formula simple, porque no vamos a necesitar precisión. Si quisiéramos ver que la conversión es correcta con un polímetro hay que ampliar el tiempo en high 

[R2526CL11_ADC_potVccgpio_2_0.py](R2526CL11_ADC_potVccgpio_2_0.py)

[R2526CL11_ADC_potVccgpio_2_1.py](R2526CL11_ADC_potVccgpio_2_1.py)

El 2.1 incluye mejoras visuales : print en la misma linea + en la excepción retorno de carro antes de mensaje

### M#3 - ADC con potenciómetro un extremo a GPIO + Display b/n SH1106

Añadimos un **display SH1106** para hacer el montaje autónomo = que no tenga que estar conectado al PC para leer valores. En los montajes #3 y #4 , seguiremos con conexión al PC para monitorear mejor.

#### Asegurar Display

Conectamos display siguiendo esquema de clase 10 del año pasado, [2425CL10_DisplayGrafSH1106](https://github.com/Jcspoza/2425CL10_DisplayGrafSH1106)

en GPIO04 y 05 para el bus I2C 0

y hacemos un check de HW con el programa basicHWtest del display sh1106

[Rbhwt_sh1106_1_0.py](Rbhwt_sh1106_1_0.py)

#### Programa M#3

Se ha subido solo la version 3.3 del programa que incluye algunas mejoras visuales, respecto a versiones mas básicas en el manejo del display (no incluidas)

[R2526CL11_ADC_pVgDisp_3_3.py](R2526CL11_ADC_pVgDisp_3_3.py)

### M#4 - ADC con potenciómetro un extremo a GPIO + Display b/n SH1106 + Letra grande y diferente con 'writer'

Si queremos un aspecto mas profesional, tenemso que poder tener tipos de letra distintos y de mas tamaños 

#### Asegurar Display + letra grande (20 x 20)

1. Instalamos la libreria 'writer.py' si no estuviera en la PICO (mejor en /lib) , 

2. copiamos la letra a usar en raiz de la pico , por ejemplo [freesans20.py](freesans20.py)

3. y hacemos un test básico 

[Rbhwt_sh1106_writer_1_0.py](Rbhwt_sh1106_writer_1_0.py)

#### Programas M#4

[R2526CL11_ADC_pVgDisp_4_0.py](R2526CL11_ADC_pVgDisp_4_0.py)

[R2526CL11_ADC_pVgDisp_4_1.py](R2526CL11_ADC_pVgDisp_4_0.py)

[R2526CL11_ADC_pVgDisp_4_2.py](R2526CL11_ADC_pVgDisp_4_2.py)

### Calibración con M#4 - cambiando potenciómetro x  Sensor humedad de suelo

**Usaremos el montaje M#4 cambiando potenciómetro por sensor de humedad de suelo con programa 4.2**

También necesitaremos un vaso de plástico con tierra seca ( inicialmente )

#### Resultados de la calibración

Tenemos un rango de 1 voltio, comenzando en 0,9 volt con la tierra seca y acabando en 1,8 con al tierra totalmente anegada

| Situacion                        | Valor voltios | Resistencia Polimetro |
| -------------------------------- | ------------- | --------------------- |
| al aire                          | 0,03 volt     |                       |
| Tierra muy seca                  | 0.92 volt     | 2,4 M ohm             |
| un poco de agua                  | 1,63 volt     | 223 k ohm             |
| Encharcada  de agua              | 1.79 volt     | 103 k ohm             |
| Maximo encharcada de agua        | 1.85 volt     |                       |
| Sensor en vaso de agua del grifo | 1,95 volt     |                       |

#### Fotos Ilustrativas

Con la **tierra seca** , el polímetro ha medido desde 8,23 Mohm a 2,4 M ohm, en el primer caso con tierra extremadamente seca, y en el segundo con tierra tomada del campo, contando que habia llovido hacia unos días, con una lectura de 0,92 volt



Las **puntas del sensor introducidas en agua del grifo** han dado **1,95 volt**, pendiente media de resitencia

| Tierra SECA Extrema - solo medida de resistencia                     | Tierra del campo (lluvias hace días) : 0,92volt y 2,4 Mohm           |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| <img src="./doc/tierra_muy_seca.jpg" title="" alt="" width="325">    | <img src="./doc/tierra_seca.jpg" title="" alt="" width="325">        |
| **Tierra con algo de humedad** 1,63 volt y 223 Kohm                  | **Tierra muy húmeda** 1,79 volt 101 Kohm                             |
| <img src="./doc/tierra_poco_humeda.jpg" title="" alt="" width="325"> | <img src="./doc/tierra_todo_humeda.jpg" title="" alt="" width="325"> |

### M#5 - Dar autonomía al montaje =  sin PC

Ahora que el display da los resultados de forma fiable, para hacer mas autonomo el montaje :

1. El **cierre del programa** ya no puede ser por teclado del PC --> pulsador de display 'BACK'. necesitamos incluir los pulsadores para comandar el programa , o al menso 1 pulsador

2. **SIN PC** : Probar con el programa en Pico con nombre 'main.py' + power bank de 5 volt o similar

---

## TO DO y Notas
