import serial

serial_port = '/dev/ttyS0'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate)
print('Serial port initialized successfully.')

try:
    while True:
        # Check if there's any data to read
        if ser.in_waiting > 0:
            try:
                # Read the data from the serial port
                data = ser.readline().decode('utf-8', errors='replace').rstrip()
                
                # Do something with the received data, such as printing it
                print("Received:", data)
            
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")
        
except KeyboardInterrupt:
    print("\nTerminated by user.")

finally:
    ser.close()
    print("Serial port closed.")