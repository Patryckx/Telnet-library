from pymodbus.server.async import ModbusTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock
import asyncio

# Crear una base de datos (almacenamiento de registros) para el servidor
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [0]*100),  # 100 registros de tipo Holding
    ir=ModbusSequentialDataBlock(0, [0]*100)   # 100 registros de tipo Input
)
context = ModbusServerContext(slaves=store, single=True)

# Crear el servidor TCP asíncrono y configurarlo en el puerto deseado
server = ModbusTcpServer(context, address=("0.0.0.0", 5020))

# Ejecutar el servidor en el bucle de eventos
loop = asyncio.get_event_loop()
loop.run_until_complete(server.serve())
