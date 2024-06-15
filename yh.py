import requests

def obtener_ip_publica_desde_privada(ip_privada):
    try:
        # Creamos la URL con la IP privada proporcionada por el usuario
        url = f"https://ipinfo.io/{ip_privada}/json"
        # Realizamos una solicitud GET a la URL
        respuesta = requests.get(url)
        # Parseamos la respuesta JSON
        datos = respuesta.json()
        # Extraemos la IP pública del diccionario obtenido
        ip_publica = datos['ip']
        return ip_publica
    except Exception as e:
        print(f"No se pudo obtener la IP pública: {e}")
        return None

# Solicitamos al usuario que ingrese la IP privada
ip_privada = input("Por favor ingresa la dirección IP privada: ").strip()

# Ejecutamos la función para obtener la IP pública desde la IP privada ingresada
ip_publica = obtener_ip_publica_desde_privada(ip_privada)
if ip_publica:
    print(f"La dirección IP pública correspondiente a la IP privada {ip_privada} es: {ip_publica}")
