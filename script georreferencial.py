from geopy.geocoders import Nominatim
from geopy.distance import distance

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="distancia_app")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def calcular_distancia(origen, destino):
    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)
    
    if coord_origen and coord_destino:
        distancia_millas = distance(coord_origen, coord_destino).miles
        distancia_km = distance(coord_origen, coord_destino).kilometers
        return distancia_millas, distancia_km
    else:
        return None, None

def main():
    print("Bienvenido al programa de cálculo de distancia entre ciudades.")
    origen = input("Ingrese la ciudad de origen (Chile): ")
    destino = input("Ingrese la ciudad de destino (Argentina): ")
    
    distancia_millas, distancia_km = calcular_distancia(origen, destino)
    
    if distancia_millas is not None and distancia_km is not None:
        print(f"\nDistancia entre {origen} y {destino}:")
        print(f"{distancia_millas:.2f} millas")
        print(f"{distancia_km:.2f} kilómetros")
        
        # Narrativa del viaje
        print(f"\nNarrativa del viaje desde {origen} hasta {destino}:")
        print(f"Usted viajará aproximadamente {distancia_millas:.2f} millas ({distancia_km:.2f} km) en auto.")
    else:
        print("No se pudo obtener la información. Verifique las ciudades ingresadas.")

if __name__ == "__main__":
    main()