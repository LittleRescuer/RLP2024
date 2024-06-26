# Little Rescuer
![Project Icon](./LittleRescuer_Icon.jpeg)

## Descripción

"Little Rescuer" es el prototipo de un robot autónomo diseñado para intervenir rápidamente en situaciones de emergencia en la carretera. Este dispositivo, con forma de automóvil compacto, está equipado con una variedad de funciones para garantizar la seguridad y el bienestar de los conductores y pasajeros involucrados en un accidente.

Cuando se produce un accidente, "Little Rescuer" se tiene que dejar en el suelo para que rápidamente se desplace y se posicione estratégicamente a 200 metros detrás del vehículo afectado.

Una vez en posición, "Little Rescuer" despliega una cámara que puede girar 180 grados, para capturar imágenes de la escena del accidente. Estas imágenes se envían de inmediato  a los contactos de emergencia designados por el conductor, proporcionando una rápida confirmación de que todos están bien. Una vez realizado el aviso, dicha cámara gira y se queda enfocando al tráfico para ir controlándolo.

Además de tomar fotografías, "Little Rescuer" activa su luz rotativa de emergencia V-16 para alertar a otros conductores sobre la presencia del accidente. Esta función ayuda a prevenir colisiones adicionales y garantiza la seguridad en la carretera.

En resumen, "Little Rescuer" es un valioso aliado en situaciones de emergencia en la carretera, ofreciendo una respuesta rápida y coordinada para proteger la seguridad y el bienestar de todos los involucrados en un accidente de tráfico, evitando situaciones de peligro al tener a peatones en la calzada.

## Librerías

- Python 3.x
- Raspberry Pi OS Lite
- OpenCV 4.8.0+

### Hardware

- [Cámara Raspberry Pi v2 - 8 Megapixels](https://tienda.bricogeek.com/accesorios-raspberry-pi/822-camara-raspberry-pi-v2-8-megapixels.html?utm_source=tienda&utm_medium=click&utm_campaign=prodrel)
- [Kit básico Raspberry Pi Zero Wifi + MicroSD 32GB](https://tienda.bricogeek.com/placas-raspberry-pi/1082-kit-basico-raspberry-pi-zero-wifi-microsd-32gb.html?search_query=raspberry+0&results=119)
- [Controlador de motores TB6612FNG](https://tienda.bricogeek.com/controladores-motores/999-controlador-de-motores-tb6612fng.html?gad_source=1&gclid=CjwKCAjwkuqvBhAQEiwA65XxQGEKl4mRS8Lng237hrTSqmpWEiZjts-D5bgiraJukbpSPVhL-e4TzRoCnqwQAvD_BwE)
- [Motor con eje ángulo recto y reductora 48:1](https://tienda.bricogeek.com/motores-dc/1048-motor-con-eje-angulo-recto-y-reductora-481.html)
- [Batería AA recargable - NiMH 2500mAh](https://tienda.bricogeek.com/baterias-lipo/315-bateria-aa-recargable-nimh-2500mah.html)
- [Base para baterías (4xAA)](https://tienda.bricogeek.com/componentes/160-base-para-baterias-4xaa.html)
- [Luz emergencia V16](https://www.amazon.es/dp/B0CPB1296V/ref=sspa_dk_detail_3?pd_rd_i=B0CPB1296V&pd_rd_w=A14s6&content-id=amzn1.sym.9c67f205-18e7-4d34-beb2-37ec708092ed&pf_rd_p=9c67f205-18e7-4d34-beb2-37ec708092ed&pf_rd_r=QXKYST03HQ85EHN8P6MJ&pd_rd_wg=sntWz&pd_rd_r=abeac907-5a0c-494a-a888-670a00a9615b&s=automotive&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1)
- [Motor servo SG90](https://www.amazon.com/-/es/DIYables-grados-Arduino-ESP8266-Raspberry/dp/B0C7BL12RG/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1L0LB8SVZ5SJ7&dib=eyJ2IjoiMSJ9.tF3g0NDLGtt5fAwiWI4hwkf0ADCXrya7qcPuXLK7m_Y9YkT4sUTy_d6LaOmDQYo0jZOIAxJn_NMLwEoQqMFkjmHtnyHt091FQk22sboJVID5xGpKN2jSJ5Q1mmV708nmdxvCeiwADP3tDwaaRClCEKu30IIIwV4ogP0hgORz-ZHXPk_QpMFjBc8yteDM50A9LWFsO2qiWLa4jL2pegiEDGwB8uZasnkRkqe0UPXYwLawewg-D_5SGVHz6-ufVBhY_vG5s5-DcdZXPyY0d3Bsbwdwx_IAoJ0sYpDvPtjhYfk.82u4GTRf0BEuKTSb3ELLK773mNGI7GOTw9fx8-Q4UIk&dib_tag=se&keywords=SERVOMOTOR%2B180%2BGRADOS&qid=1709728209&sprefix=servomotor%2B180%2Bgrados%2Caps%2C170&sr=8-5&th=1)
- [Antena GPS (SIM808)](https://www.amazon.com/-/es/SIM808-SIM908-desarrollo-disponible-arduino/dp/B0CJ7VSG82/ref=sr_1_1?_mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2N80TQJYI0UXU&dib=eyJ2IjoiMSJ9.hXv-p_xSEM7DAyEPmF8S9rntLb2fWXF45txRj4ajJs8J286V2FJjNUfeByuo2se3afE2-jE6zZhEJy-JdfspT8qRc2CKxvUgImxmeibZuPeULHREtyX-DdVPMcpXsO9BS6HVFriIcqRNj-L-dr1pQ.C77Y681pZcTeAl57demFS5VB_7dXKyhEeCcjzLODxB4&dib_tag=se&keywords=SIM908&qid=1709727934&s=sporting-goods&sprefix=sim908%2Csporting-intl-ship%2C163&sr=1-1)
- [Power Bank 10000mAh Dual 2.4A Cargador de Banco de Energía de Alta Velocidad Entrada USB-C Paquete de Bater ía Externa para Teléfono Celular iPhone 12 iPad Samsung S21 Huawei Xiaomi etc](https://www.amazon.es/10000mAh-Cargador-Energ%C3%ADa-Velocidad-Tel%C3%A9fono/dp/B09K3BQBW6/ref=sr_1_11?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3OMWEL1JOVABO&dib=eyJ2IjoiMSJ9.Vdk9NA-TqhAZ7Ba5BsrwliKNJTF832vjMHPGJBVkolGPGQieMDjSgVieXlwNvTlDr6x8R5nyqlxjLOJKlP9IU2XHVlecU7w4H_yYHi2p63pfYoXv68PLTgfhjFQ9B1w1F7eZ3LQwrOu1Z85h8v0u78oIK7V0-rQUWGI1O7HaqJ4h8g-zjzQkZcMglZz60j8LcAJC5YVTGg26YLCZFfHatUrzrxcefKZkBt3NFkkzB3giYmqHm7NvFvKR_dPm3Ehj885Qxu10wxCk-52GtFx0sYchFD8EXSemQovuvXtULpM.Re02CkR7yzbGIx-qBL01_aJLekveOBQ498wtp5VZzKA&dib_tag=se&keywords=power%2Bbank%2B2%2C5a%2B5v&qid=1710930248&sprefix=power%2Bbank%2B2%2B5a%2B5v%2Caps%2C98&sr=8-11&th=1)
- [Cable USB C a Micro USB](https://www.amazon.com/-/es/flexible-soporta-sincronizaci%C3%B3n-compatible-MacBook/dp/B0BX5G8WNZ/ref=sr_1_5?crid=PH82Y5PL6LAS&dib=eyJ2IjoiMSJ9.85K-eyJjWT0MAs6p-6W9GREkk6xK8f6zTZdz6GZvL04CgCJWGR1idHnKwx4sKF22ftCbnOK6LJJBkmOTdD8THtXEDg80_U6EUX6N1EEw3JelCgAL1DAKpEPsohoMG8dOxmkRr-Y9xce8-n6DpROXzvFz5R2Bvw3Q4MrRbcZDlR5qP_3Cq4WM8iikfGiGzBB_oNkKkJni_Kmu18wHWJqw7IZiPVfVOcxTV0yDkzsII30.op-QSihLrfOppXYToA9V57npy248FMzIhSJlL578jeA&dib_tag=se&keywords=microusb%2Bto%2Busb%2Bc&qid=1710930565&sprefix=microusb%2Bto%2Caps%2C209&sr=8-5&th=1)


### Schematic
![Schematic](./Schematics/Esquema_DC_DualMotor+Servo.png)

### 3D

Se pueden encontrar los componentes 3D  [aquí](./Modelo/Componenetes%20Chasis)

### Diagrama de arquitectura del Software
![Diagrama de arquitectura del Software del proyecto LittleRescuer (UAB)](./Modelo/SW_Architecture/SW_Architecture_v2.png)

### Agradecimientos

Queremos agradecer a nuestros 3 profesores de la asignatura:

- Fernando Luis Vilariño Freire
- Carlos García Calvo
- Vernon Stanley Albayeros Duarte

Gracias a su apoyo, este proyecto ha podido superar todos sus altibajos y llegar a buen término con éxito. Estamos agradecidos por el apoyo y la orientación brindada por nuestros profesores a lo largo de este proyecto. Durante los momentos críticos, ofrecieron su experiencia y conocimientos, permitiéndonos encontrar soluciones efectivas.

## Refs
Los proyectos que hemos usado como referencia son:
[1](https://www.instructables.com/Autonomous-Autonavigation-Robot-Arduino/)
[2](https://www.instructables.com/Self-Driving-Car-Using-Arduinoautonomous-Guided-Ve/)
[3](https://github.com/AtsushiSakai/PythonRobotics)
[4](https://github.com/dctian/DeepPiCar)

