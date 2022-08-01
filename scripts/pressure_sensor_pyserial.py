import serial  
import datetime 
# configure the serial connections (the parameters differs on the device you are connecting to)


COM_PORT = '/dev/ttyACM0'    
BAUD_RATES = 9600   

ser = serial.Serial(
    port=COM_PORT,
    baudrate=BAUD_RATES,
)

try:
    while True:
        while ser.in_waiting:
            current_time = datetime.datetime.now()
            data_raw = ser.readline()  
            data = data_raw.decode()   
            print("time different ", datetime.datetime.now()-current_time)
            print("raw_data", data_raw)
            print("collected", data)
            

except KeyboardInterrupt:
    ser.close()    
    print("disconnect")