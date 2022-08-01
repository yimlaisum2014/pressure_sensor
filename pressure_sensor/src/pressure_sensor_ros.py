#!/usr/bin/env python

import rospy
# import serial

class PressuerSensor():
    def __init__(self):
        self.port_1 = '/dev/ttyACM0'    
        self.baud_rate = 9600
        self_serial_1 = None

        self.connect()
        
    def connect(self):
        self.serial_1 = serial.Serial(port=self.port_1,
                    baudrate=self.baud_rate,
                )
        print(self.serial_1.in_waiting)
        if self.serial_1.in_waiting > 0:
            print("connected")

    def read_pressure_data(self):
        serial_1_data = self.serial_1.readline().decode()
        print("data : ",serial_1_data)
        return serial_1_data


if __name__ == "__name__" :
    rospy.init_node("stream_pressure",anonymous=False)
    

    pressure = PressuerSensor

    rospy.Timer(rospy.Duration(1/10.0),pressure.read_pressure_data)

    rospy.spin()