import socket
import json
import threading
import time

HOST = '127.0.0.1'
PORT = 5005

def recibir(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print("\nPosición recibida desde Unity:", data.decode('utf-8'))
        except:
            break

def enviar(sock):
    while True:
        try:
            print("\n--- Ingrese nuevas posiciones de agentes ---")
            n = int(input("¿Cuántos agentes quieres mover? "))
            agentes = []
            for _ in range(n):
                agent_id = input("ID del agente (ejemplo agent_0): ")
                x = float(input("X: "))
                y = float(input("Y: "))
                z = float(input("Z: "))
                agentes.append({"id": agent_id, "x": x, "y": y, "z": z})
            posiciones = {"agents": agentes}
            msg = json.dumps(posiciones).encode('utf-8')
            sock.sendall(msg)
            print("Mensaje enviado:", posiciones)
        except Exception as e:
            print("Error enviando datos:", e)
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print("Conectado a Unity")

   
    threading.Thread(target=recibir, args=(sock,), daemon=True).start()
    
    enviar(sock)

if __name__ == "__main__":
    main()
