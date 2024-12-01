import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import defines
#create modbus server 

server=modbus_tcp.TcpServer(address="0.0.0.0" ,port=502)


slave=server.add_slave(1)


slave.add_block("holding",defines.HOLDING_REGISTERS,0,100)
slave.set_values("holding",0,[0]*100)

slave.add_block("coils",defines.COILS,0,100)
slave.set_values("coils",0,[0]*100)

print("server inicialized")
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("server stop")

server.stop()