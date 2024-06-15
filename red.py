from scapy.all import ARP, Ether, srp
import argparse

def analizar_dispositivo(ip):
    # Construir la solicitud ARP para la IP específica
    arp = ARP(pdst=ip)

    # Capa Ethernet para la solicitud ARP
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp

    # Enviar la solicitud ARP y obtener la respuesta
    resultado = srp(paquete, timeout=3, verbose=0)[0]

    if resultado:
        # Extraer y devolver la dirección MAC del dispositivo
        return resultado[0][1].hwsrc
    else:
        return None

if __name__ == "__main__":
    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Analizar un dispositivo en la red mediante su dirección IP")
    parser.add_argument('ip', help='Dirección IP del dispositivo a analizar')
    args = parser.parse_args()

    ip = args.ip

    # Analizar el dispositivo
    print(f"Analizando dispositivo con IP: {ip}")
    direccion_mac = analizar_dispositivo(ip)

    if direccion_mac:
        print(f"Dirección MAC encontrada: {direccion_mac}")
    else:
        print("No se encontró ningún dispositivo activo con esa IP en la red.")
