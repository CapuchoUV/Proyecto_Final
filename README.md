# Monitor de Temperatura y Humedad con GrovePi

Sistema de monitoreo de temperatura y humedad usando Raspberry Pi, sensor DHT y pantalla LCD, con almacenamiento en base de datos MySQL.

## 📋 Descripción

Este proyecto lee datos de temperatura y humedad de un sensor DHT conectado a un GrovePi, muestra los valores en una pantalla LCD RGB y los almacena en una base de datos MySQL para su análisis posterior.

## Componentes Necesarios

- Raspberry Pi
- GrovePi/GrovePi+
- Sensor DHT (azul - DHT11 o blanco - DHT22)
- Pantalla LCD RGB Grove
- Cables de conexión Grove

## 📦 Requisitos de Software

```bash
# Librerías de Python
- grovepi
- grove_rgb_lcd
- MySQLdb (mysql-connector-python)
```

### Instalación de Dependencias

```bash
# Instalar GrovePi
curl -kL dexterindustries.com/update_grovepi | bash

# Instalar MySQL connector
pip install mysql-connector-python
# o
pip install mysqlclient
```

## 🗄️ Configuración de la Base de Datos

Crear la base de datos y tabla en MySQL:

```sql
CREATE DATABASE tempmds;

USE tempmds;

CREATE TABLE datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temp VARCHAR(10),
    humedad VARCHAR(10),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Crear el usuario de MySQL:

```sql
CREATE USER 'helman'@'localhost' IDENTIFIED BY '4321';
GRANT ALL PRIVILEGES ON tempmds.* TO 'helman'@'localhost';
FLUSH PRIVILEGES;
```

## 🔌 Conexiones de Hardware

- **Sensor DHT**: Conectar al puerto **D7** del GrovePi
- **Pantalla LCD RGB**: Conectar a un puerto **I2C** del GrovePi

## ⚙️ Configuración del Código

Antes de ejecutar, ajusta estos parámetros según tu configuración:

```python
dht_sensor_port = 7  # Puerto del sensor DHT
dht_sensor_type = 0  # 0 para DHT11 (azul), 1 para DHT22 (blanco)

# Credenciales de MySQL
conexion = MySQLdb.connect(
    host='localhost',
    user='helman',      # Cambia por tu usuario
    passwd='4321',      # Cambia por tu contraseña
    db='tempmds'        # Nombre de tu base de datos
)
```

## 🚀 Uso

Ejecutar el programa:

```bash
python3 temp_humidity_monitor.py
```

Para detener el programa, presiona `Ctrl + C`.

## 📊 Funcionamiento

1. **Lectura**: El sensor DHT lee temperatura y humedad cada 0.05 segundos
2. **Visualización**: Los datos se muestran en la pantalla LCD con fondo verde
3. **Almacenamiento**: Cada lectura se guarda automáticamente en MySQL
4. **Monitoreo**: Los datos también se imprimen en la consola

### Ajustar el intervalo de lectura

```python
sleep(0.05)  # Cambiar el valor (en segundos)
```

## Manejo de Errores

El programa maneja automáticamente:

- Errores de lectura del sensor (valores NaN)
- Errores de conexión a la base de datos
- Interrupciones del usuario (Ctrl+C)

## 📝 Ejemplo de Salida

temp = 25.0 C    humidity = 60.0 %
Datos guardados: Temp = 25.0 C, Humedad = 60.0 %
temp = 25.1 C    humidity = 59.8 %
Datos guardados: Temp = 25.1 C, Humedad = 59.8 %
