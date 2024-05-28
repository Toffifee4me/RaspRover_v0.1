# echo-server.py

import socket
from gpiozero import Motor, OutputDevice, Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

HOST = "10.0.0.115"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

motor1 = Motor(24, 27)
factory = PiGPIOFactory()

motor1_enable = OutputDevice(5, initial_value=1)
servoGPIO = 26
servo = Servo(servoGPIO, pin_factory=factory)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            if data.__eq__(b"GoUp"):
                motor1.forward()
                sleep(3)
                motor1.stop()
                print("done")
            if data.__eq__(b"GoTest"):

                servo.mid()
                print("mid")
                sleep(0.5)
                servo.min()
                print("min")
                sleep(1)
                servo.mid()
                print("mid")
                sleep(0.5)
                servo.max()
                print("max")
                sleep(1)
            conn.sendall(data)
