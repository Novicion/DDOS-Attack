# 📚 Proyecto Educativo

Bienvenido/a a este **pequeño proyecto educativo**, diseñado especialmente para personas interesadas en aprender y practicar ciberseguridad. 🎉 

---

## 🧐 ¿De qué se trata?
Este proyecto tiene como objetivo ayudarte a comprender como es un ataque de DDOS. 💻✨ 

> ⚠️ **DISCLAIMER:** Este proyecto es únicamente para fines educativos y de investigación en ciberseguridad. No está destinado para uso malicioso. El uso de este script sin autorización del propietario del sistema objetivo es ilegal y puede acarrear sanciones graves. El autor no se hace responsable del mal uso de este script.

---

## 🚀 Cómo comenzar
Sigue estos sencillos pasos para poner en marcha el proyecto en tu entorno local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Novicion/DDOS-Attack.git

# 🛠️ Herramientas utilizadas
   - Lenguaje: Python 
   - Librerías: threading, socket

# 📫 Contacto
   Si tienes preguntas o sugerencias, no dudes en escribirme:
      **✉️ noviciondev@gmail.com**

## **What Does the Script Do?**
The script simulates a **DDoS attack** (Distributed Denial of Service) by:
1. Creating multiple threads to simulate high traffic.
2. Sending a large number of HTTP requests to overwhelm the target server.
3. Using a fake IP address to disguise the origin of the traffic.

This kind of attack is used maliciously to disrupt the availability of websites or services. However, here it is provided solely to demonstrate how such attacks function.

---

## **How to Mitigate a DDoS Attack**

### 1. **Filter Suspicious Traffic**
- Use firewall rules to block malicious IPs.
- Example using `iptables`:
  ```bash
  sudo iptables -A INPUT -s 182.21.20.32 -j DROP
  ```

---

### 2. **Rate Limiting**
- Configure servers to limit the number of requests from a single IP.
- Example with **Nginx**:
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

### 3. **Use Specialized Services**
- Employ DDoS protection services like **Cloudflare**, **Akamai**, or **AWS Shield** to filter traffic and absorb large-scale attacks.

---

### 4. **Load Balancing**
- Distribute traffic across multiple servers using load balancers like **HAProxy**.

---

### 5. **Content Delivery Networks (CDN)**
- Use CDNs such as **Cloudflare** or **Fastly** to offload traffic to distributed servers.

---

### 6. **Validate Incoming Requests**
- Implement CAPTCHA or challenge-response mechanisms to verify users.

---

### 7. **Monitoring and Alerts**
- Use tools like **Zabbix**, **Prometheus**, or **Grafana** to detect abnormal traffic patterns.
- Set up alerts for unusual traffic spikes.

---

### 8. **Optimize Server Resources**
- Increase server capacity (CPU, RAM, bandwidth).
- Adjust server connection limits:
  Example for **Apache**:
  ```conf
  <IfModule mpm_prefork_module>
      MaxClients 100
      MaxRequestsPerChild 1000
  </IfModule>
  ```

---

### 9. **SYN Cookies**
- Protect against SYN flood attacks by enabling SYN cookies:
  ```bash
  sudo sysctl -w net.ipv4.tcp_syncookies=1
  ```

---

### 10. **Segment and Redundancy**
- Divide your infrastructure into segments and use redundant systems.

---

## **Example: Detect and Block Malicious IPs**

```python
import os
from collections import Counter

log_file = "/var/log/access.log"  # Path to the web server access log

def detect_suspicious_ips():
    with open(log_file, "r") as file:
        ips = [line.split()[0] for line in file]
    ip_counts = Counter(ips)
    for ip, count in ip_counts.items():
        if count > 100:  # Threshold for suspicious activity
            block_ip(ip)

def block_ip(ip):
    print(f"Blocking IP: {ip}")
    os.system(f"iptables -A INPUT -s {ip} -j DROP")

detect_suspicious_ips()
```

---

## **Legal Note**
Sharing this script aligns with GitHub's policies on ethical cybersecurity education. Ensure you:
- Use this in **controlled environments only** (e.g., virtual machines, private networks).
- Include this disclaimer in any distribution of this project.

## **License**
This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.
