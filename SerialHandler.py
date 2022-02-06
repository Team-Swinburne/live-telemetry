from turtle import end_fill
import serial.tools.list_ports

class Serial_Emulator:
    def __init__(self):
        self.__available_ports = []

    def get_available_port(self):
        self.ports = serial.tools.list_ports.comports()
        print(self.ports)
        for port in sorted(self.ports):
            self.__available_ports.append(port.device)
        return self.__available_ports      

d = Serial_Emulator()
print(d.get_available_port())
