# 🛡️ SOC Home Lab

**Laboratorios de ciberseguridad defensiva, monitorización e investigación de eventos.**

Este repositorio reúne prácticas realizadas en un entorno de laboratorio autorizado y aislado, con énfasis en el trabajo de un analista SOC: recopilación de evidencias, análisis de registros, investigación de alertas y conclusiones sustentadas.

> **Estado del repositorio:** en construcción. Los laboratorios se marcan como finalizados cuando cuentan con resultados comprobados y documentación.

## 🧪 Índice de laboratorios

| ID | Laboratorio | Enfoque | Estado |
| --- | --- | --- | --- |
| LAB-SOC-001 | [Ping Me — Network Forensics & SOC Monitoring](labs/LAB-SOC-001-Ping-Me/README.md) | Tráfico ICMP, análisis PCAP, detección con Suricata y monitorización con Wazuh | 🟢 Finalizado y verificado |

**Leyenda:** ⚪ Planificado · 🟡 En desarrollo · 🟢 Finalizado y verificado.

## 🗂️ Estructura

```text
SOC-Home-Lab/
├── README.md
├── labs/
│   └── LAB-SOC-001-Ping-Me/
│       ├── README.md                  # Informe y resultados del laboratorio
│       ├── diagrams/README.md         # Topología documentada
│       ├── screenshots/               # Capturas de evidencia
│       ├── configs/local.rules        # Firma personalizada de Suricata
│       └── analysis/
│           ├── README.md
│           ├── ping_me_lab.py         # Generador de tráfico ICMP de prueba
│           └── trafico.pcapng         # Captura de paquetes
└── templates/
    └── LAB-TEMPLATE.md
```

## 🔎 Metodología de documentación

Cada laboratorio documenta su objetivo, entorno, procedimiento, evidencias, interpretación SOC y conclusiones. Las detecciones observadas no se presentan como incidentes confirmados sin evidencia adicional.

No se publican credenciales, tokens, claves privadas ni secretos de configuración.

## ✍️ Publicaciones

Los artículos explicativos podrán compartirse en [Medium — @csm24](https://medium.com/@csm24). Los **write-ups de CTF** se mantienen en un [repositorio separado](https://github.com/CesarSoria2224/CTF-Writeups).

---

[← Volver al perfil de César Soria](https://github.com/CesarSoria2224)
