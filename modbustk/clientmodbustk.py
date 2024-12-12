import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines

# Crear cliente Modbus TCP
client = modbus_tcp.TcpMaster(host="192.168.0.102", port=502)
client.set_timeout(5.0)

try:
    # Leer 10 bobinas desde la dirección 0
    start_address = 0  # Dirección inicial
    quantity = 10      # Número de bobinas a leer
    coils = client.execute(1, defines.READ_COILS, start_address, quantity)
    print(f"Valores leídos de las bobinas desde {start_address}: {coils}")

    # Escribir en una sola bobina
    coil_address = 2  # Dirección de la bobina
    value_to_write = 1  # Valor a escribir (1 para activar, 0 para desactivar)
    client.execute(1, defines.WRITE_SINGLE_COIL, coil_address, output_value=value_to_write)
    print(f"Escrito {value_to_write} en la bobina {coil_address}")

    # Escribir en múltiples bobinas
    start_address = 6  # Dirección inicial
    values_to_write = [1, 0, 1, 1, 0]  # Valores a escribir
    client.execute(1, defines.WRITE_MULTIPLE_COILS, start_address, output_value=values_to_write)
    print(f"Escritos {values_to_write} en las bobinas desde {start_address}")

    # Leer nuevamente las bobinas para verificar los cambios
    updated_coils = client.execute(1, defines.READ_COILS, 0, 10)
    print(f"Valores actualizados de las bobinas desde 0: {updated_coils}")

except modbus_tk.modbus.ModbusError as e:
    print(f"Error Modbus: {e}")

except Exception as e:
    print(f"Error general: {e}")

finally:
    client.close()

