from pymodbus.client import ModbusTcpClient
# Configuración de conexión
hmi_ip = "192.168.0.102"  # Dirección IP de la HMI
hmi_port = 502            # Puerto Modbus TCP
client = ModbusTcpClient(hmi_ip, port=hmi_port)

# Conectar al HMI
if client.connect():
    print("Conexión establecida con la HMI.")

    # Enviar un valor a un registro específico (ejemplo: dirección 40001)
    register_address = 0  # Dirección Modbus (40001 en decimal es 0 en pymodbus)
    value_to_send = 123   # Valor que deseas enviar
    result = client.write_register(register_address, value_to_send)

    if result.isError():
        print("Error al enviar datos.")
    else:
        print("Datos enviados con éxito.")

    # Cerrar la conexión
    client.close()
else:
    print("No se pudo conectar a la HMI.")