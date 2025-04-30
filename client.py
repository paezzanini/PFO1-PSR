import socket

# Configuración del socket cliente
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    return client_socket

# Ejecución principal del cliente
if __name__ == "__main__":
    try:
        client_socket = connect_to_server()
        print("Conectado Exitosamente. Escribí los mensajes:")
        
        while True:
            message = input("> ")
            if message.lower() == "exit":
                print("Saliendo...")
                break
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {response}")
        
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")
