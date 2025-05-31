import socket
def start_server():
    Mi_socket = socket.socket()
    Mi_socket.bind(('localhost', 8001))  # port 8001 to avoid conflicts
    Mi_socket.listen(5)
    print("Servidor iniciado y escuchando en localhost:8001")
    while True:
        conexion, addr = Mi_socket.accept()
        print("Nueva conexión establecida desde", addr)
        peticion = conexion.recv(1024)
        print("Mensaje recibido:", peticion.decode())  # decode bytes to string
        conexion.send("Bienvenido al servidor".encode())  # encode string to bytes
        conexion.close()
if __name__ == "__main__":
    start_server()