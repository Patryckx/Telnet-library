import socket
import logging

class TCPClient:
    """
    Una clase para manejar conexiones TCP/IP con un dispositivo.
    """
    def __init__(self, host: str, port: int, buffer_size: int = 1024, timeout: int = 10):
        """
        Inicializa el cliente TCP/IP.
        
        :param host: Dirección IP o hostname del dispositivo.
        :param port: Puerto del dispositivo.
        :param buffer_size: Tamaño del buffer para recepción de datos.
        :param timeout: Tiempo de espera en segundos para las operaciones.
        """
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.client_socket = None

    def connect(self):
        """
        Establece la conexión con el dispositivo.
        """
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.settimeout(self.timeout)
            self.client_socket.connect((self.host, self.port))
            logging.info(f"Conectado al dispositivo en {self.host}:{self.port}")
        except (socket.timeout, socket.error) as e:
            logging.error(f"Error al conectar con {self.host}:{self.port} - {e}")
            raise

    def send_data(self, data: bytes):
        """
        Envía datos al dispositivo.
        
        :param data: Datos en formato bytes que se desean enviar.
        """
        if not self.client_socket:
            raise ConnectionError("No hay una conexión activa.")
        
        try:
            self.client_socket.sendall(data)
            logging.info(f"Datos enviados: {data}")
        except socket.error as e:
            logging.error(f"Error al enviar datos - {e}")
            raise

    def receive_data(self) -> bytes:
        """
        Recibe datos del dispositivo.
        
        :return: Datos recibidos en formato bytes.
        """
        if not self.client_socket:
            raise ConnectionError("No hay una conexión activa.")
        
        try:
            data = self.client_socket.recv(self.buffer_size)
            logging.info(f"Datos recibidos: {data}")
            return data
        except socket.error as e:
            logging.error(f"Error al recibir datos - {e}")
            raise

    def disconnect(self):
        """
        Cierra la conexión con el dispositivo.
        """
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
            logging.info("Conexión cerrada.")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Configuración del dispositivo
    host = "192.168.1.202"  # Dirección IP del dispositivo
    port = 8500             # Puerto del dispositivo

    # Crear instancia del cliente TCP
    client = TCPClient(host, port)

    try:
        # Conectar al dispositivo
        client.connect()

        # Enviar datos
        mensaje = b"Hola, dispositivo"
        client.send_data(mensaje)

        # Recibir respuesta
        respuesta = client.receive_data()
        print(f"Respuesta del dispositivo: {respuesta.decode('utf-8')}")

    except Exception as e:
        logging.error(f"Se produjo un error: {e}")

    finally:
        # Desconectar
        client.disconnect()
