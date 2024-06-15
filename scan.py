import socket

def check_port(hostname, port):
    try:
        # Intentamos crear un socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de conexión en segundos

        # Intentamos conectar al host y puerto especificados
        result = sock.connect_ex((hostname, port))

        if result == 0:
            print(f"El puerto {port} en {hostname} está abierto")
        else:
            print(f"El puerto {port} en {hostname} está cerrado o filtrado")

        sock.close()  # Cerramos el socket
    except socket.error as e:
        print(f"Error al conectar con el puerto {port} en {hostname}: {e}")

def main():
    while True:
        try:
            # Pedimos al usuario que ingrese la dirección IP o hostname
            hostname = input("Ingresa la dirección IP o el hostname (deja vacío para salir): ")
            if not hostname:
                break  # Salimos del bucle si no se ingresa nada

            # Pedimos al usuario que ingrese el número de puerto
            port_str = input("Ingresa el número de puerto: ")
            port = int(port_str)  # Convertimos el input a entero

            # Verificamos el puerto utilizando la función check_port
            check_port(hostname, port)
        except ValueError:
            print("Error: El número de puerto debe ser un entero.")
        except KeyboardInterrupt:
            print("\n\nProceso interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
