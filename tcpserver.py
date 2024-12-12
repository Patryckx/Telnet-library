from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification

# Crear un datastore para los registros de ejemplo
def create_server():
    # Creamos un contexto para los registros de holding (10 registros)
    slave_context = ModbusSlaveContext(
        hr=[0]*10  # 10 holding registers inicializados en 0
    )

    # Creamos un contexto para el servidor con un único esclavo (ID 1)
    context = ModbusServerContext(slaves={1: slave_context}, single=True)

    # Definir la identificación del dispositivo Modbus
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'My Vendor'
    identity.ProductCode = '123'
    identity.VendorUrl = 'http://myvendor.com'
    identity.ProductName = 'Modbus Server Example'
    identity.ModelName = 'MyDevice'
    identity.MajorMinorRevision = '1.0.0'

    # Iniciar el servidor Modbus TCP en localhost y puerto 5020
    StartTcpServer(context=context, identity=identity, address=("localhost", 5020))

if __name__ == "__main__":
    create_server()
