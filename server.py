import socket
import sqlite3
import threading
from datetime import datetime
from db_handler import save_message

# Configuración del socket TCP/IP, puede tener hasta 5 conexiones en cola de espera
def initialize_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    print("Servidor iniciado en localhost:5000")
    return server_socket

# Aceptar conexiones entrantes de clientes
def accept_connections(server_socket):
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Nueva conexión desde {client_address}")
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
        except Exception as e:
            print(f"Error al aceptar la conexión: {e}")

# Manejar la comunicación con el cliente
def handle_client(client_socket, client_address):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            save_message(message, client_address[0])
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = f"Mensaje recibido: {timestamp}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error al manejar al cliente {client_address}: {e}")
    finally:
        client_socket.close()

# Ejecución principal del servidor - Ejecuta el socket y tiene manejo de errores generales
if __name__ == "__main__":
    try:
        server_socket = initialize_socket()
        accept_connections(server_socket)
    except socket.error as e:
        print(f"Error de socket: {e}")
    except sqlite3.Error as e:
        print(f"Error en la Base de Datos: {e}")
    except Exception as e:
        print(f"Error general: {e}")
