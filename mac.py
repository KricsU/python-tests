import platform
import getpass
import subprocess
import socket
import psutil
import requests
from datetime import datetime

def obtener_info_mac(ip):
    try:
        # Obtener nombre de host
        nombre_host = socket.gethostbyaddr(ip)[0]
        print(f"Hostname: {nombre_host}")

        # Información del sistema operativo
        sistema_operativo = platform.system()
        version_sistema = platform.mac_ver()[0]
        print(f"Sistema Operativo: {sistema_operativo} ({version_sistema})")

        # Obtener el nombre de usuario actual
        usuario_actual = getpass.getuser()
        print(f"Usuario Actual: {usuario_actual}")

        # Obtener el navegador predeterminado (en macOS)
        navegador = subprocess.check_output(["defaults", "read", "-g", "com.apple.Safari", "WebKitDefaultWebBrowser"]).strip().decode()
        print(f"Navegador Predeterminado: {navegador}")

        # Información de CPU
        cpu_info = f"CPU: {psutil.cpu_count()} cores, {psutil.cpu_freq().current}MHz"
        print(cpu_info)

        # Información de memoria
        mem_info = f"Memoria: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        print(mem_info)

        # Información de discos
        disco_info = "Discos:"
        for disco in psutil.disk_partitions():
            disco_info += f"\n  - Dispositivo: {disco.device}, Punto de Montaje: {disco.mountpoint}"
        print(disco_info)

        # Estado del PC
        estado_pc = f"Uso de CPU: {psutil.cpu_percent(interval=1)}%, Uso de Memoria: {psutil.virtual_memory().percent}%"
        print(estado_pc)

        # Localización basada en IP
        url = f"http://ip-api.com/json/{ip}"
        respuesta = requests.get(url)
        datos = respuesta.json()
        if datos["status"] == "success":
            print(f"Localización: {datos['city']}, {datos['regionName']}, {datos['country']}")
        else:
            print("No se pudo obtener la localización.")

        # Obtener aplicaciones instaladas (en macOS usando system_profiler)
        salida = subprocess.check_output(["system_profiler", "SPApplicationsDataType"]).decode()
        print("Aplicaciones Instaladas:")
        print(salida)

        # Obtener usuarios del sistema (en macOS)
        salida = subprocess.check_output(["dscl", ".list", "/Users"]).decode().splitlines()
        print("Usuarios del Sistema:")
        for usuario in salida:
            print(usuario)

        # Obtener horario del sistema
        ahora = datetime.now()
        print(f"Hora del Sistema: {ahora}")

    except Exception as e:
        print(f"Error al obtener la información en macOS: {str(e)}")

# Ejemplo de uso para macOS:
ip = input("Introduce una dirección IP de macOS: ")
obtener_info_mac(ip)
