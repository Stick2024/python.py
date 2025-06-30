import socket
def start_client():
    Mi_socket = socket.socket()
    Mi_socket.connect(('localhost', 8001))
    mensaje = "hola desde el cliente"
    Mi_socket.send(mensaje.encode())  # encode string to bytes
    respuesta = Mi_socket.recv(1024)
    print("Respuesta del servidor:", respuesta.decode())  # decode bytes to string
    Mi_socket.close()
if __name__ == "__main__":
    start_client()