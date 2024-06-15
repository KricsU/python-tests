import socket

def enviar_mensaje(ip, mensaje):
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al dispositivo en la dirección IP especificada y puerto 12345
        sock.connect((ip, 12345))

        # Enviar el mensaje codificado en bytes
        sock.sendall(mensaje.encode())

        # Esperar la respuesta (opcional)
        respuesta = sock.recv(1024)
        print(f'Respuesta del dispositivo en {ip}: {respuesta.decode()}')

    except ConnectionRefusedError:
        print(f"No se pudo conectar al dispositivo en {ip}")

    finally:
        # Cerrar el socket
        sock.close()

if __name__ == "__main__":
    # Pedir al usuario que ingrese la dirección IP del dispositivo
    ip = input("Ingrese la dirección IP del dispositivo: ")

    # Mensaje a enviar
    mensaje = "Hola desde Python"

    # Llamar a la función para enviar el mensaje
    enviar_mensaje(ip, mensaje)
