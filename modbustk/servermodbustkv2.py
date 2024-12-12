import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines

# Crear servidor Modbus TCP
#server = modbus_tcp.TcpServer(address="192.168.0.102", port=502)
server = modbus_tcp.TcpServer(address="0.0.0.0", port=502)

# Añadir un esclavo con ID 1
slave = server.add_slave(1)

# Añadir bloques de registros de retención (holding registers) y bobinas (coils)

# Bloque de registros holding (0x03) - 100 registros
slave.add_block("holding", defines.HOLDING_REGISTERS, 0, 100)  # 100 registros
slave.set_values("holding", 0, [0] * 100)  # Inicializar con ceros

# Bloque de bobinas (coils) (0x01) - 100 bobinas
slave.add_block("coils", defines.COILS, 0, 100)  # 100 bobinas
slave.set_values("coils", 0, [0] * 100)  # Inicializar con ceros

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
