import sqlite3
from datetime import datetime

# Guardar el mensaje en la base de datos SQLite
def save_message(content, client_ip):
    connection = sqlite3.connect('chat_messages.db')
    cursor = connection.cursor()
    
    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        )
    ''')
    
    # Insertar el mensaje en la tabla
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO messages (contenido, fecha_envio, ip_cliente)
        VALUES (?, ?, ?)
    ''', (content, timestamp, client_ip))
    
    connection.commit()
    connection.close()
