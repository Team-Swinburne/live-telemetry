
import serial.tools.list_ports
import serial
import serial.threaded

class Serial_Emulator:
    def __init__(self):
        self.__available_ports = []

    #Gets all the available ports
    def get_available_port(self):
        self.ports = serial.tools.list_ports.comports()

        for port in sorted(self.ports):
            self.__available_ports.append(port.device)

        return self.__available_ports 

    #Opens the port at the specified baudrate
    def OpenPort(self, Port, BaudRate):
        self.SerialConnection = serial.Serial(Port, BaudRate, timeout=0.1) 
        a = serial.threaded.LineReader()

    #Closes the port
    def ClosePort(self):
        self.SerialConnection.close()
        self.SerialConnection.__del__()

    #Reads a line and correctly formats suchs as removing \r\n
    def Read(self):
        return self.SerialConnection.readline().decode('utf-8')[:-3]



#d = Serial_Emulator()
#print(d.get_available_port())
