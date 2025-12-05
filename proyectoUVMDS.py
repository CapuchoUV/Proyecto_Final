from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import MySQLdb

dht_sensor_port = 7  # connect the DHt sensor to port 7
dht_sensor_type = 0  # use 0 for the blue-colored sensor and 1 for the white-colored sensor

conexion = MySQLdb.connect(host='localhost', user='helman', passwd='4321', db='tempmds')
curs = conexion.cursor()

setRGB(0, 255, 0)

while True:
    try:
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum, "%")
        
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')
        
        t = str(temp)
        h = str(hum)
        
        curs.execute("INSERT INTO datos(temp, humedad) VALUES (%s, %s)", (t, h))
        
        conexion.commit()
        print("Datos guardados: Temp =", t, "C, Humedad =", h, "%")
        
        setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")
        
        sleep(0.05)
        
    except (IOError, TypeError) as e:
        print("Error de sensor:", str(e))
        setText("")
        
    except MySQLdb.Error as e:
        print("Error de base de datos:", e)
        try:
            conexion.rollback()
        except:
            pass
        setText("")
        
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        setText("")
        break

print("Cerrando conexión a la base de datos")
conexion.close()