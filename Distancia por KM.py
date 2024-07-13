# Importamos la librería necesaria para calcular distancias
from geopy.distance import great_circle

# Definimos una función para calcular la distancia entre dos ciudades
def calcular_distancia(ciudad_origen, ciudad_destino):
    # Ejemplo de coordenadas, se pueden cambiar según las ciudades
    coordenadas_origen = (-33.4489, -70.6693)  # Santiago, Chile
    coordenadas_destino = (-34.6037, -58.3816)  # Buenos Aires, Argentina
    
    distancia = great_circle(coordenadas_origen, coordenadas_destino).miles  # Distancia en millas
    
    return distancia

# Función para calcular la duración del viaje (ejemplo)
def calcular_duracion(distancia, medio_transporte):
    # Ejemplos de velocidad promedio en diferentes medios de transporte (en millas por hora)
    if medio_transporte == 'auto':
        velocidad_promedio = 60
    elif medio_transporte == 'avion':
        velocidad_promedio = 500
    else:
        velocidad_promedio = 30  # Suponiendo otro medio de transporte
        
    tiempo_horas = distancia / velocidad_promedio
    tiempo_minutos = tiempo_horas * 60
    
    return tiempo_horas, tiempo_minutos

# Función para mostrar la narrativa del viaje
def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, tiempo_horas, tiempo_minutos, medio_transporte):
    print(f"Narrativa del Viaje:")
    print(f"------------------")
    print(f"Viajando desde {ciudad_origen} a {ciudad_destino}:")
    print(f"- Distancia: {distancia:.2f} millas")
    if medio_transporte == 'auto':
        print(f"- Duración del viaje en auto: aproximadamente {tiempo_horas:.1f} horas ({tiempo_minutos:.0f} minutos)")
        print(f"  Recorrerás la ruta terrestre por carreteras y caminos, disfrutando de paisajes variados.")
    elif medio_transporte == 'avion':
        print(f"- Duración del viaje en avión: aproximadamente {tiempo_horas:.1f} horas ({tiempo_minutos:.0f} minutos)")
        print(f"  Experimentarás un vuelo cómodo y rápido, disfrutando de vistas aéreas de las ciudades y paisajes.")
    else:
        print(f"- Duración del viaje en otro medio de transporte: aproximadamente {tiempo_horas:.1f} horas ({tiempo_minutos:.0f} minutos)")
        print(f"  Elige tu medio de transporte preferido y disfruta del viaje entre estas dos increíbles ciudades.")
    print(f"------------------")

# Función principal del programa
def main():
    print("Bienvenido al calculador de viajes entre ciudades de Chile y Argentina.")
    
    while True:
        ciudad_origen = input("Por favor ingrese la ciudad de origen ('s' para salir): ")
        if ciudad_origen.lower() == 's':
            print("¡Hasta luego!")
            break
        
        ciudad_destino = input("Por favor ingrese la ciudad de destino ('s' para salir): ")
        if ciudad_destino.lower() == 's':
            print("¡Hasta luego!")
            break
        
        distancia = calcular_distancia(ciudad_origen, ciudad_destino)
        
        print("\nPor favor elija el tipo de medio de transporte:")
        print("1. Auto")
        print("2. Avión")
        print("3. Otro")
        opcion = input("Elija una opción (1/2/3) ('s' para salir): ")
        if opcion.lower() == 's':
            print("¡Hasta luego!")
            break
        
        if opcion == '1':
            medio_transporte = 'auto'
        elif opcion == '2':
            medio_transporte = 'avion'
        else:
            medio_transporte = 'otro'
        
        tiempo_horas, tiempo_minutos = calcular_duracion(distancia, medio_transporte)
        
        mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, tiempo_horas, tiempo_minutos, medio_transporte)

# Ejecutamos el programa
if __name__ == "__main__":
    main()