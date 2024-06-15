import requests
import json

def geolocalizar_ip(ip):
    try:
        # Construimos la URL con la IP proporcionada por el usuario
        url = f"https://ipinfo.io/{ip}/json"
        
        # Realizamos una solicitud GET a la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la solicitud no tiene éxito
        
        # Parseamos la respuesta JSON
        datos = respuesta.json()
        
        # Extraemos los datos de geolocalización
        ciudad = datos.get('city', 'Desconocida')
        region = datos.get('region', 'Desconocida')
        pais = datos.get('country', 'Desconocido')
        ubicacion = datos.get('loc', 'Desconocida')
        
        # Imprimimos la información de geolocalización
        print(f"Geolocalización para la IP {ip}:")
        print(f"Ciudad: {ciudad}")
        print(f"Región: {region}")
        print(f"País: {pais}")
        print(f"Ubicación (latitud, longitud): {ubicacion}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud HTTP: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
    except KeyError as e:
        print(f"Error: No se encontró la clave en los datos JSON.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Solicitamos al usuario que ingrese la IP a geolocalizar
ip = input("Por favor ingresa la dirección IP a geolocalizar: ").strip()

# Ejecutamos la función para geolocalizar la IP ingresada
geolocalizar_ip(ip)
