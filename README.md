🖥️ Python Remote Access Tool (RAT)
A fully functional Remote Access Tool (RAT) built in Python that allows secure remote command execution, file system control, screen sharing, webcam access, system monitoring, and more. This project demonstrates the power of socket programming, multithreading, and remote control protocols using Python.

🚀 Features
✅ Server-Side (Command Center)
Interactive Command Shell: Remotely execute CMD commands on the client.

File System Access: Upload, download, delete, edit, and move files.

Registry Editing: Create, set, and delete registry keys.

Video Surveillance: Live webcam stream, snapshot, and screen sharing via vidstream.

Screenshot Capture: Grab screen images instantly.

System Control: Shutdown, reboot, monitor off/on, task manager toggle, etc.

Input Devices: Disable/enable keyboard and mouse.

Keylogger Control: Start/stop keylogger and fetch logs.

Network Monitoring: Scan ports, get Wi-Fi profiles and passwords.

Geolocation Retrieval: Locate client machine via IP.

✅ Client-Side
Command Receiver: Listens for and executes server commands securely.

System Information Reporting: Sends detailed info on OS, CPU, time, etc.

Webcam & Screen Streaming: Captures and streams live video to the server.

Screenshot & Snapshot: Captures screen or webcam on demand.

Security and Admin Status Check: Verify if user has admin rights.

🔧 Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/unethicalHacker1/RAT-Remote-Access-Torjan-
cd your-repo-name
2. Install Dependencies
Server:
bash
Copy code
pip install -r server_requirements.txt
Client:
bash
Copy code
pip install -r client_requirements.txt
3. Run the System
Start the Server:
bash
Copy code
python server.py
Start the Client (on target system):
bash
Copy code
python client.py
Make sure both use the same host and port.

📁 Project Structure

File	Description
server.py	Remote control shell interface (RAT server)
client.py	Command receiver & executor with stream
server_requirements.txt	Python packages for server functionality
client_requirements.txt	Python packages for client functionality
⚠️ Disclaimer
This tool is developed strictly for educational purposes and authorized remote administration. Do not use it for unethical or illegal activities. The author holds no responsibility for any misuse.

👤 Author
Made with Python by Soban Saeed
For learning, experimenting, and secure remote system management.
