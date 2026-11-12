# Configuración de detección

- [local.rules](local.rules): firma personalizada de Suricata utilizada en LAB-SOC-001.

La regla `sid:1000001` identifica solicitudes ICMP Echo Request (`itype:8`, `icode:0`) con un payload de exactamente dos bytes (`dsize:2`).

Es una firma específica de laboratorio; una coincidencia no demuestra por sí sola exfiltración o actividad maliciosa.

[← Volver al informe](../README.md)
