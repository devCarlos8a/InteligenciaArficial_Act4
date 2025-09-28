# Sistema de simulacion de rutas de transmilenio (Ruta --> Bogotá - Funza)

## 📌 Problema planteado
Una persona necesita trasladarse desde **Bogotá a Funza**, pero no conoce la mejor ruta para hacerlo.  

Este sistema:
- Conoce las conexiones entre diferentes estaciones.  
- Calcula los tiempos de viaje.  
- Encuentra la **ruta más rápida automáticamente** para proporcionársela al usuario.  

## Definición del sistema

En la función crear_sistema() definimos lo que el sistema va a aprender para conocer las rutas, tiempos y destinos.  

Además, el sistema contabiliza:
- El **tiempo transcurrido** al realizar un trasbordo.  
- La **cantidad de trasbordos** que realiza el usuario.  

## Cálculo de trasbordos:

if self.lineas[actual] != self.lineas[siguiente]:
    nuevo_tiempo += 5
    nuevo_trasbordo += 1

## Búsqueda de la mejor ruta

El siguiente bloque implementa el iterador principal.
Aquí el sistema: Comienza en un origen, explora todos los nodos o rutas como posibles opciones, escoge la ruta más eficiente, evita retornar a lugares por donde ya pasó.

while cola_rutas:
    tiempo, actual, ruta, trasbordo = heapq.heappop(cola_rutas)
    if actual in visitados:
        continue
    visitados.add(actual)
    
    if actual == destino:
        return Ruta(ruta, tiempo, trasbordo)
    
    # búsqueda de conexiones desde la estación en cola
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


Al llegar al destino, el sistema garantiza que la ruta encontrada es la más óptima para el usuario, considerando tanto el tiempo total de viaje como la cantidad de trasbordos.
