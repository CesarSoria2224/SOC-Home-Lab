# LAB-SOC-001 — Ping Me

**Estado: 🟡 En desarrollo**  
**Área:** Network Forensics / SOC Monitoring  
**Entorno:** VMware, red aislada de laboratorio

## 1. Objetivo

Analizar tráfico ICMP generado de forma controlada y explorar cómo registrar, investigar y correlacionar la actividad desde la perspectiva de un SOC. El laboratorio todavía no tiene resultados finales validados.

## 2. Arquitectura prevista

| Sistema | IP de laboratorio | Función |
| --- | --- | --- |
| Kali Linux | `192.168.10.2` | Emisión controlada de tráfico de prueba con Scapy |
| Windows 10 Pro | `192.168.10.3` | Equipo supervisado por Wazuh Agent |
| Ubuntu Server | `192.168.10.100` | Wazuh 4.14.9 |
| Red VMware | `192.168.10.0/24` | Segmento aislado |

## 3. Estado de avance

- [x] Preparación de máquinas y red de laboratorio, según registro de progreso.
- [x] Integración inicial del agente Wazuh en Windows, según registro de progreso.
- [x] Preparación del script para generar tráfico ICMP de prueba.
- [ ] Ejecutar y registrar la prueba ICMP.
- [ ] Capturar y analizar el tráfico con Wireshark; guardar evidencias PCAP revisadas.
- [ ] Validar si los eventos necesarios se observan desde Wazuh; documentar límites y ajustes si aplica.
- [ ] Redactar hallazgos, interpretación SOC y conclusiones.

> **Importante:** instalar Wazuh Agent no implica que el tráfico ICMP esté siendo detectado automáticamente. La visibilidad de red se evaluará y se documentará con evidencias.

## 4. Evidencias y documentación

- [Diagramas](diagrams/README.md)
- [Capturas](screenshots/README.md)
- [Configuración](configs/README.md)
- [Análisis](analysis/README.md)

## 5. Resultados

**Pendientes de verificación.** No se incluyen hallazgos ni alertas no comprobados.

## 6. Publicaciones

El artículo de Medium se enlazará aquí cuando exista y se haya contrastado con las evidencias.

[← Índice SOC Home Lab](../../README.md)
