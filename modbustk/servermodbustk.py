import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines

# Crear servidor Modbus TCP
#server = modbus_tcp.TcpServer()

server = modbus_tcp.TcpServer(address="192.168.0.102", port=502)

# Añadir un esclavo
slave = server.add_slave(1)

# Añadir un bloque de registros de tipo holding (registros de retención)
slave.add_block("holding", defines.HOLDING_REGISTERS, 0, 10)  # 10 registros
slave.set_values("holding", 0, [0]*10)  # Inicializar los registros con 0
slave.set_values("holding", 0, [1])
# Iniciar el servidor
print("Servidor Modbus TCP corriendo en 192.168.0.102:502...")
server.start()

# Mantener el servidor en ejecución
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Servidor detenido.")

# Detener el servidor cuando se presione Ctrl+C
server.stop()
