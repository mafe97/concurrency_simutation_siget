import threading
import time
import random

# Configuración del Buffer del SIGET
BUFFER_SIZE = 5
buffer = []

# Semáforos de Sincronización [1, 4]
mutex = threading.Semaphore(1)      # Exclusión mutua para acceso al buffer
empty = threading.Semaphore(BUFFER_SIZE) # Cuenta espacios vacíos
full = threading.Semaphore(0)       # Cuenta espacios ocupados

class SensorTrafico(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        while True:
            dato = random.randint(10, 90) # Simula flujo vehicular
            empty.acquire() # wait(empty) [1]
            mutex.acquire() # wait(mutex) - Sección Crítica [4]
            
            buffer.append(dato)
            print(f"[+] {self.nombre} envió dato: {dato} veh/min. Buffer: {len(buffer)}")
            
            mutex.release() # signal(mutex) [1]
            full.release()  # signal(full)
            time.sleep(random.uniform(0.5, 2))

class ModuloAnalisis(threading.Thread):
    def run(self):
        while True:
            full.acquire()  # wait(full)
            mutex.acquire() # wait(mutex)
            
            dato = buffer.pop(0)
            print(f"    [-] Analizador procesó: {dato}. Buffer restante: {len(buffer)}")
            
            mutex.release() # signal(mutex)
            empty.release() # signal(empty)
            time.sleep(random.uniform(1, 3))

# Inicialización de hilos concurrentes [5, 6]
sensor1 = SensorTrafico("Sensor_Norte")
sensor2 = SensorTrafico("Sensor_Sur")
analizador = ModuloAnalisis()

sensor1.start()
sensor2.start()
analizador.start()