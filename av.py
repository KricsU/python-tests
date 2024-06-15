import socket

def check_antivirus(ip):
    common_ports = {
        "ClamAV": [3310],
        "McAfee": [8081],
        "Avast": [21, 22],
        "Norton": [80, 443],
        "Bitdefender": [21],
        "AVG": [4158],  # Puerto típico para AVG
        "Malwarebytes": [443],  # Puerto típico para Malwarebytes
        "Windows Defender": [135, 445],  # Puertos típicos para Windows Defender
        "Kaspersky": [13000],  # Puerto típico para Kaspersky
        # Puedes añadir más antivirus y sus puertos aquí según sea necesario
    }

    results = {}

    for antivirus, ports in common_ports.items():
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Tiempo de espera para la conexión
            result = sock.connect_ex((ip, port))
            if result == 0:
                if antivirus not in results:
                    results[antivirus] = []
                results[antivirus].append(port)
            sock.close()

    if results:
        print(f"Antivirus encontrados en {ip}:")
        for antivirus, ports in results.items():
            print(f"{antivirus} en puertos: {', '.join(map(str, ports))}")
    else:
        print(f"No se encontraron antivirus en {ip}.")

if __name__ == "__main__":
    ip = input("Introduce la dirección IP a escanear: ")
    check_antivirus(ip)
