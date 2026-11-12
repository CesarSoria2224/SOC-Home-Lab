
from scapy.all import IP, ICMP, Raw, send
import time

DESTINO = "192.168.10.3"
MENSAJE = "SOC-LAB-001"

print("[+] Iniciando laboratorio Ping Me")

for numero, caracter in enumerate(MENSAJE, start=1):
    datos = caracter.encode("ascii") + b"\x00"

    paquete = (
        IP(dst=DESTINO)
        / ICMP(type=8, code=0, seq=numero)
        / Raw(load=datos)
    )

    send(paquete, verbose=False)
    print(f"Paquete {numero}: {datos.hex()}")
    time.sleep(1)

print("[+] Simulacion terminada")

