# iot11

### Descripción
* Sistema IoT enfocado a los sensores que contiene un coche, que se encarga de recolectar información sobre ellos, mostrarlos por pantalla para poder monitorearlos con el fin de mejorar la eficiencia energética del coche, mejorar la experiencia y facilitar la conducción del usuario.

* Algunos ejemplos de estos sensores pueden ser los sensores de activación de luces automáticas, los sensores que miden la presión de los neumáticos (barómetro) o los sensores del nivel de combustible. El propósito fundamental de este sistema es tener la capacidad de manejar estos sensores y modificarlos a gusto del usuario/a.

#### Caso de uso / escenario típico de la vida real para ilustrar la idea.

* Basándose en el nivel de iluminación ambiente, el coche regula la luz de los faros.
* Cuando la presión de los neumáticos sea mayor o menor a la establecida el sensor detecta esta diferencia, y activa un led en la pantalla del conductor.
* Cuando esté lloviendo, el sensor detecta el nivel de agua que cae al cristal delantero y regula la potencia del limpiaparabrisas.
* Cuando el nivel del depósito del combustible haya bajado el límite establecido el sensor lo detecta y activa un led en la pantalla del conductor.
* El usuario introduce una velocidad por pantalla para cuando se supere este límite el sensor emita un sonido detectando que este límite se ha superado. 
* Cuando el coche esté a una distancia reducida de cualquier objeto el sensor lo reconoce y emite un pitido constante que aumenta al ir acercándose a este objeto. De la misma manera este pitido se verá reducido a medida que se vaya alejando del sensor.

#### Ventajas del sistema propuesto comparado con otras alternativas en el mercado o ya existentes.

* Configuración de sensores: Cuando empieza a limpiar, a cuanta distancia suenan los sensores de proximidad o a cuanta temperatura empieza a calentar el modo automático.
* Los datos de los sensores se visualizan en la pantalla del coche para poder monitorearlos y saber las condiciones actuales de ellos, cosa que no se suele ver en la mayoría de sistemas de vehículos que no sean gama alta.
* Ayuda a mejorar el consumo de energía del vehículo, que hoy en día dada la transición a coches eléctricos tiende a ser importante y aunque existen no suelen estar disponibles para el usuario.

### Versión actual (11/01/2022)
En esta versión, se ejecuta el proyecto y se puede hacer uso de dos funcionalidades mediante llamadas REST por Postman:
* Una de ellas percibe a través de los sensores de temperatura y humedad, distancia y luz, y dependiendo de la configuración establecida responde mediante mensajes escritos en una pantalla LCD, zumbidos y la luz de un led respectivamente.   
* La otra funcionalidad sirve para que te devuelva la información que captan los sensores de temperatura y humedad, distancia y luz.

Además, guarda los datos recibidos por los sensores en la base de datos de Corlysis y es posible visualizarlos en Grafana.

## Arquitectura
Un breve resumen de la estructura de clases:
### API
Metodos que pueden ser llamados desde, por ejemplo, Postman.
### Routes
Nombra las diferentes rutas principales para hacer llamadas a API. En este proyecto, solo usamos */iot/*. 
### Services
* *data_sender.py*: recibe datos y los envía a Corlysis para que sean almacenados.
* *main_service.py*: procesa la funcionalidad de "ejecución continua" llamando a los métodos de los sensores, también sirve para parar el proceso. 
* *sensores.py*: es donde se recogen y se procesan los datos de los sensores.
### config.py
Se guardan los valores de las variables generales, por ejemplo el puerto para las llamadas de API, la URL de Corlysis o donde van conectados los sensores.
### run.py
El fichero a ejecutar para poner el proyecto en marcha.

## Getting Started
### Prerrequisitos
* Python 3
* Raspberry Pi con Linux
* Grove - Light Sensor V1.2
* Grove - LCD Display (Blue and White)
* Grove - Temperature and Humidity Sensor(DHT11)
* Grove - Buzzer
* Grove - Red Led Button
* Grove - Ultrasonic Ranger
* Postman

### Clonar proyecto
* El proyecto se puede clonar desde el enlace *https://github.com/enekoperez/iot11* o desde la terminal con el siguiente comando:
```
git clone https://github.com/enekoperez/iot11
```

## Getting Ready
Para prepararlo, hay que entrar con la Raspberry Pi en el directorio donde esta el proyecto y ejecutar el fichero *run.py*:
1. Para abrir el directorio:
```
cd iot11
```
2. Para instalar las dependencias:
```
pip install -r requirements.txt
```
3. Para ejecutar el fichero:
```
python3 run.py
```

### Ejecutar el proyecto
Una vez abierto y ejecutado el fichero run.py, existen dos principales funcionalidades: 
* Ejecución continua
* Llamadas a la API del proyecto

Para ambas es necesario abrir Postman, importar el fichero JSON del proyecto *postman_vXX-XX-XXXX.json*. 

Dentro de la colección *iot* existen varias posibilidades de *request*, por ejemplo *execute*, donde la URL es *http://192.168.1.134:3000/iot/execute*. Es necesario cambiar, en este caso, 192.168.1.134 por la dirección IP de la Raspberry Pi.

#### 1. Ejecución continua
La ejecución continua trata de recibir información de los sensores, tratarlo y almacenarlo de forma ininterrumpida, para esto se debe ejecutar el *request* *execute* desde Postman.

Este método permite establecer mediante JSON la configuración para recibir los resultados y que los sensores actúen de distintas maneras, por ejemplo:
```
{
    "conf_distance_cerca":"20",
    "conf_distance_lejos":"60",
    "conf_luz":"400",
    "conf_temp":"25",
    "conf_humi":"100"
}
```
* Todos los campos deben ser rellenados. 
* La distancia está en centímetros, la temperatura en °C y el grado de humedad en porcentaje.

Cuando se quiera parar este proceso, se debe ejecutar el *request* *ender* desde Postman.

#### 2. Llamadas a la API del proyecto
El proyecto también permite recibir llamadas a cada sensor para devolver los datos que pueden proporcionar estos. Existe la posibilidad de llamar a los siguientes sensores:
* Temperatura y humedad con el *request* *temp and hum* desde Postman, que devuelve por ejemplo:
```
{
    "humi": 56,
    "temp": 20
}
```
* Distancia con el *request* *distance* desde Postman, que devuelve por ejemplo:
```
{
    "distance": 215.7934780778556
}
```
* Luz con el *request* *light* desde Postman, que devuelve por ejemplo:
```
{
    "light": 609
}
```

### Bluetooth
* El bluetooth funciona a través de la librería bluez y utilizando pybluez para conectar el bluetooth de la raspberri pi con el bluetooth del móvil a una aplicación llamada (serial bluetooth) para poder enviar texto, o en nuestro caso encoded text para pasar las variables de los sensores al móvil por bluetooth en caso de necesitar una medición puntual del sensor.

* Hay que tener en cuenta que hemos de emparejar los dispositivos antes de realizar cualquiera de estos pasos, desde las raspberri pi al móvil.

* Para poder realizar la conexión, tenemos que ejecutar el programa python que abre una terminal en raspian desde la raspberri pi que abre un puerto a una conexión para enlazar el bluetooth serial a nuestro móvil. Desde esta aplicación pulsamos en la raspi para terminar de conectar y formar el vínculo bluetooth. Una vez realizado el vínculo, al ejecutar el sensor desde el programa que contiene el bluetooth añadido en linea de código (la llamada al método), se enviará la medición de este sensor al móvil.
