import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines

# Crear cliente Modbus TCP
client = modbus_tcp.TcpMaster(host="192.168.0.102", port=502)

# Crear cliente Modbus TCP
#client = modbus_tcp.TcpMaster(host="192.168.0.102", port=502)



# Leer los primeros 10 registros de tipo holding
result = client.execute(1, modbus_tk.defines.READ_HOLDING_REGISTERS, 0, 10)
print("Valores leídos de los registros:", result)


# Escribir en una sola bobina
coil_address = 2  # Dirección de la bobina
value_to_write = 1  # Valor a escribir (1 para activar, 0 para desactivar)
client.execute(1, defines.WRITE_SINGLE_COIL, coil_address, output_value=value_to_write)
print(f"Escrito {value_to_write} en la bobina {coil_address}")


# Escribir en una sola bobina
coil_address = 3  # Dirección de la bobina
value_to_write =1  # Valor a escribir (1 para activar, 0 para desactivar)
client.execute(1, defines.WRITE_SINGLE_COIL, coil_address, output_value=value_to_write)
print(f"Escrito {value_to_write} en la bobina {coil_address}")


# Escribir en una sola bobina
coil_address = 1  # Dirección de la bobina
value_to_write = 1  # Valor a escribir (1 para activar, 0 para desactivar)
client.execute(1, defines.WRITE_SINGLE_COIL, coil_address, output_value=value_to_write)
print(f"Escrito {value_to_write} en la bobina {coil_address}")
