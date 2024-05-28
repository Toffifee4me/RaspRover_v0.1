# echo-client.py

import socket
import keyboard

HOST = "10.0.0.115"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    keyboard.on_press_key("w", lambda _: s.sendall(b"GoUp"))
    keyboard.on_press_key("a", lambda _: s.sendall(b"GoLeft"))
    keyboard.on_press_key("s", lambda _: s.sendall(b"GoBack"))
    keyboard.on_press_key("d", lambda _: s.sendall(b"GoRight"))
    keyboard.on_press_key("p", lambda _: s.sendall(b"GoTest"))
    while True:
        data = s.recv(1024)
        print(f"Received {data!r}")

p