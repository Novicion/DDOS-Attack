
# 📚 Proyecto Educativo

Bienvenido/a a este **proyecto educativo**, diseñado especialmente para personas interesadas en aprender y practicar ciberseguridad. 🎉

---

## 🧐 ¿De qué se trata?
Este proyecto tiene como objetivo ayudarte a comprender cómo funciona un ataque de DDoS (Denegación de Servicio Distribuida). 💻✨ 

> ⚠️ **DISCLAIMER:**  
> Este proyecto es únicamente para fines educativos y de investigación en ciberseguridad. No está destinado para uso malicioso.  
> **El uso de este script sin autorización del propietario del sistema objetivo es ilegal** y puede acarrear sanciones graves.  
> El autor no se hace responsable del mal uso de este script.

---

## 🚀 Cómo comenzar
Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Novicion/DDOS-Attack.git
   ```

2. **Instala los requisitos necesarios:**  
   Este script utiliza Python y las librerías `threading` y `socket`, incluidas por defecto en Python.

---

## 🛠️ ¿Qué hace el script?
Este script simula un **ataque DDoS** básico al:
1. Crear múltiples hilos para simular tráfico masivo.
2. Enviar una gran cantidad de solicitudes HTTP para saturar el servidor objetivo.
3. Usar una IP falsa para ocultar el origen del tráfico.

⚠️ **Nota:** Aunque este tipo de ataques se usa maliciosamente para interrumpir servicios, este proyecto tiene fines educativos para demostrar cómo funcionan y cómo defenderse de ellos.

---

## 🛡️ Cómo mitigar un ataque DDoS

### 1. **Filtrar tráfico sospechoso**
- Usa reglas de firewall para bloquear IPs maliciosas.
- Ejemplo con `iptables`:
  ```bash
  sudo iptables -A INPUT -s 182.21.20.32 -j DROP
  ```

---

### 2. **Limitar la tasa de solicitudes (Rate Limiting)**
- Configura tu servidor para limitar la cantidad de solicitudes desde una IP en un período de tiempo.
- Ejemplo con **Nginx**:
  ```nginx
  http {
      limit_req_zone $binary_remote_addr zone=one:10m rate=30r/s;
      server {
          location / {
              limit_req zone=one;
          }
      }
  }
  ```

---

### 3. **Usar servicios especializados**
- Implementa servicios como **Cloudflare**, **Akamai** o **AWS Shield** para filtrar tráfico y absorber ataques a gran escala.

---

### 4. **Balanceo de carga**
- Distribuye el tráfico entre varios servidores para evitar la saturación de uno solo.
- Herramientas recomendadas: **HAProxy**.

---

### 5. **Redes de entrega de contenido (CDN)**
- Usa CDNs como **Cloudflare** o **Fastly** para reducir la carga directa en el servidor principal.

---

### 6. **Validar solicitudes entrantes**
- Implementa sistemas como CAPTCHA para confirmar que las solicitudes provienen de usuarios legítimos y no de bots.

---

### 7. **Monitoreo y alertas**
- Usa herramientas como **Zabbix**, **Prometheus** o **Grafana** para detectar patrones de tráfico anómalos.
- Configura alertas automáticas para picos de tráfico inusuales.

---

### 8. **Optimización del servidor**
- Incrementa los recursos del servidor (CPU, RAM, ancho de banda).
- Ajusta los límites de conexión en el servidor:
  Ejemplo en **Apache**:
  ```conf
  <IfModule mpm_prefork_module>
      MaxClients 100
      MaxRequestsPerChild 1000
  </IfModule>
  ```

---

### 9. **Cookies SYN**
- Protege tu servidor contra ataques de tipo SYN flood activando cookies SYN:
  ```bash
  sudo sysctl -w net.ipv4.tcp_syncookies=1
  ```

---

### 10. **Segmentación y redundancia**
- Divide tu infraestructura en segmentos y usa sistemas redundantes para reducir el impacto de un ataque.

---

## 📜 Ejemplo: Detectar y bloquear IPs maliciosas

```python
import os
from collections import Counter

log_file = "/var/log/access.log"  # Ruta al archivo de logs del servidor web

def detect_suspicious_ips():
    with open(log_file, "r") as file:
        ips = [line.split()[0] for line in file]
    ip_counts = Counter(ips)
    for ip, count in ip_counts.items():
        if count > 100:  # Umbral de solicitudes sospechosas
            block_ip(ip)

def block_ip(ip):
    print(f"Bloqueando IP: {ip}")
    os.system(f"iptables -A INPUT -s {ip} -j DROP")

detect_suspicious_ips()
```

---

## ⚖️ Nota legal
El propósito de este proyecto es alinear el aprendizaje con las políticas éticas de ciberseguridad.  
**Úsalo únicamente en entornos controlados** (e.g., máquinas virtuales, redes privadas) y siempre incluye esta advertencia en cualquier distribución.

---

## 📫 Contacto
Si tienes preguntas o sugerencias, no dudes en escribirme:  
✉️ **noviciondev@gmail.com**

