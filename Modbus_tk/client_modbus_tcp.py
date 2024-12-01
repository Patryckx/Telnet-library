import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines

# Crear cliente Modbus TCP
client = modbus_tcp.TcpMaster(host="192.168.0.102", port=502)
client.set_timeout(5.0)

try:
    # Escribir un valor en un registro holding (registro 0)
    register_address = 0  # Dirección del registro
    value_to_write = 1234  # Valor a escribir
    client.execute(1, defines.WRITE_SINGLE_REGISTER, register_address, output_value=value_to_write)
    print(f"Escrito {value_to_write} en el registro {register_address}")

    # Escribir múltiples valores en registros holding (registros 1-3)
    start_address = 1  # Dirección inicial
    values_to_write = [100, 200, 300]  # Valores a escribir
    client.execute(1, defines.WRITE_MULTIPLE_REGISTERS, start_address, output_value=values_to_write)
    print(f"Escritos {values_to_write} en los registros a partir de {start_address}")

    # Leer los registros holding para verificar la escritura
    result = client.execute(1, defines.READ_HOLDING_REGISTERS, 0, 10)
    print("Valores leídos de los registros:", result)

except modbus_tk.modbus.ModbusError as e:
    print(f"Error Modbus: {e}")

except Exception as e:
    print(f"Error general: {e}")

finally:
    client.close()
