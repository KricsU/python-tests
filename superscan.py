import socket

def escanear_puertos(hostname):
    # Resolver el nombre de host a una dirección IP
    try:
        target_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"No se pudo resolver el hostname '{hostname}'")
        return

    print(f"Escaneando puertos en {target_ip} ({hostname})...")

    # Rango de puertos a escanear (1-65535)
    puerto_inicial = 1
    puerto_final = 65535

    puertos_vulnerables = []

    for puerto in range(puerto_inicial, puerto_final + 1):
        # Crear un socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Tiempo máximo de espera para conexión

        # Intentar conectar al puerto
        resultado = sock.connect_ex((target_ip, puerto))
        
        if resultado == 0:
            print(f"Puerto {puerto}: Abierto")
            puertos_vulnerables.append(puerto)
        else:
            print(f"Puerto {puerto}: Cerrado o no accesible")
        
        sock.close()

    # Mostrar lista de puertos vulnerables al final del escaneo
    if puertos_vulnerables:
        print("\nPuertos vulnerables encontrados:")
        print(", ".join(map(str, puertos_vulnerables)))
    else:
        print("\nNo se encontraron puertos vulnerables.")

# Pedir al usuario que ingrese el hostname o la dirección IP
hostname = input("Introduce el hostname o la dirección IP: ")

# Llamar a la función de escaneo de puertos
escanear_puertos(hostname)
