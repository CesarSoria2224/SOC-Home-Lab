# Topología del laboratorio

La topología está documentada mediante una tabla en la [sección 4 del informe](../README.md#4-topología-de-red); no se requiere un diagrama de imagen adicional.

| Equipo | IP | Función |
| --- | --- | --- |
| Kali Linux | `192.168.10.2` | Generador de tráfico de prueba |
| Windows 10 Pro | `192.168.10.3` | Destino ICMP |
| Ubuntu Server 24.04.5 | `192.168.10.100` | Suricata IDS y Wazuh |

Red virtualizada aislada: `192.168.10.0/24`.

[← Volver al informe](../README.md)
