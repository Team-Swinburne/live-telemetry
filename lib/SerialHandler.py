from turtle import end_fill
import serial.tools.list_ports
import serial
import serial.threaded
import struct

class SerialEmulator:
    def __init__(self):
        self.__available_ports = []
        self.rxBuffer = []
        self.rxState = 0
        self.rxPacketLength = 0
        self.rxPacketCount = 0

    #Gets all the available ports
    def get_available_port(self):
        self.ports = serial.tools.list_ports.comports()

        for port in sorted(self.ports):
            self.__available_ports.append(port.device)

        return self.__available_ports 

    #Opens the port at the specified baudrate
    def OpenPort(self, Port, BaudRate):
        self.SerialConnection = serial.Serial(Port, BaudRate, timeout=0.1) 
        self.SerialConnection.flushInput()
        #a = serial.threaded.LineReader()

    #Closes the port
    def ClosePort(self):
        self.SerialConnection.close()
        self.SerialConnection.__del__()

    #Reads a line and correctly formats suchs as removing \r\n
    def Read(self):
        rxData = []
        rxByte = struct.unpack('B', self.SerialConnection.read(1))[0]
        match self.rxState:
            case 0: #idle
                if (rxByte == 0x19):
                    self.rxState +=1
            case 1: #1st start flag found
                if (rxByte == 0x94):
                    self.rxState += 1
                    self.rxBuffer.clear()
                    rxData.clear()
            case 2: #2nd start flag found
                self.rxPacketLength = rxByte
                self.rxState += 1
            case 3: #found both start flag and length
                self.rxPacketCount += 1
                if (self.rxPacketCount < self.rxPacketLength):
                    self.rxBuffer.append(rxByte)
                else:
                    self.rxBuffer.append(rxByte)
                    self.rxState += 1
                    rxData = self.rxBuffer.copy()
            case _:
                self.rxState = 0
                self.rxPacketCount = 0
                self.rxPacketLength = 0


        return rxData#self.SerialConnection.readline().decode().strip()



#d = Serial_Emulator()
#print(d.get_available_port())
