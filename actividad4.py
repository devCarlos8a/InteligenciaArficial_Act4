from dataclasses import dataclass
from typing import List, Dict, Optional
import heapq

#Definimos la clase Ruta para almacenar la información de la ruta encontrada
@dataclass
class Ruta:
    estaciones: List[str]
    tiempo_total: int
    trasbordo: int


# Esta clase representa el sistema de trasmilenio y contiene los métodos para agregar estaciones, conectar estaciones y buscar rutas.
class sistema_Trasmilenio:
    def __init__(self):
        self.conexiones = {}
        self.lineas = {}
        
    def agregar_estacion(self, estacion: str, linea: str):
        self.lineas[estacion] = linea
        if estacion not in self.conexiones:
            self.conexiones[estacion] = []
    
    def conectar(self, origen: str, destino: str, tiempo: int):
        self.conexiones[origen].append((destino, tiempo))
        self.conexiones[destino].append((origen, tiempo))
    
    def buscar_ruta(self, origen: str, destino: str) -> Optional[Ruta]:
        if origen == destino:
            return Ruta([origen], 0, 0)
            
        cola_rutas = [(0, origen, [origen], 0)]
        visitados = set()
        
        while cola_rutas:
            tiempo, actual, ruta, trasbordo = heapq.heappop(cola_rutas)
            
            if actual in visitados:
                continue
            visitados.add(actual)
            
            if actual == destino:
                return Ruta(ruta, tiempo, trasbordo)
            
            # busqueda de conexiones desde la estacion en cola
            for siguiente, tiempo_viaje in self.conexiones.get(actual, []):
                if siguiente not in visitados:
                    nuevo_tiempo = tiempo + tiempo_viaje
                    nueva_ruta = ruta + [siguiente]
                    nuevo_trasbordo = trasbordo
                    
                    if len(ruta) > 1 and self.lineas[actual] != self.lineas[siguiente]:
                        nuevo_tiempo += 5
                        nuevo_trasbordo += 1
                    
                    heapq.heappush(cola_rutas, (nuevo_tiempo, siguiente, nueva_ruta, nuevo_trasbordo))
        
        return None

# conexiones y estaciones del trasmilenio predeterminadas
def crear_sistema():
    transmilenio = sistema_Trasmilenio()
    
    transmilenio.agregar_estacion("Bogota", "Norte")
    transmilenio.agregar_estacion("Soacha", "Norte")
    transmilenio.agregar_estacion("Facatativa", "Occidental")
    transmilenio.agregar_estacion("Funza", "Occidental")
    transmilenio.agregar_estacion("Usme", "Norte")
    transmilenio.agregar_estacion("Chia", "Norte")
    transmilenio.agregar_estacion("Centro", "Conexión")
    
    transmilenio.conectar("Bogota", "Centro", 20)
    transmilenio.conectar("Centro", "Soacha", 7)
    transmilenio.conectar("Centro", "Facatativa", 5)
    transmilenio.conectar("Facatativa", "Funza", 10)
    transmilenio.conectar("Centro", "Usme", 20)
    transmilenio.conectar("Usme", "Chia", 8)
    
    return transmilenio

# Llamando a la funcion principal para conocer la ruta entre Bogota y Funza
if __name__ == "__main__":
    sistema = crear_sistema()
    
    origen = "Bogota"
    destino = "Funza"
    
    ruta = sistema.buscar_ruta(origen, destino)

# finalmente imprime la ruta encontrada    
    if ruta:
        print(f"Ruta: {' → '.join(ruta.estaciones)}")
        print(f"Tiempo: {ruta.tiempo_total} minutos")
        print(f"trasbordo: {ruta.trasbordo}")
    else:
        print("Sin ruta")