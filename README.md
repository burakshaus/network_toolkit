Network Tools & Web-Based Chat Project
Overview
This project consists of two independent parts implemented in Python:

Part A: GUI-Based Network Toolkit (70% weight)
A modular toolkit providing several network-related utilities via a graphical interface using tkinter. Users can access different tools such as port scanning, web crawling, file transfer, Wikipedia summary fetching, network scanning, and broadcast messaging.

Part B: Web-Based Real-Time Chat Application (30% weight)
A simple web chat system using Python’s built-in HTTP and WebSocket servers to allow real-time communication via a browser without external frameworks.

Part A – GUI-Based Network Toolkit
Features
Port Scanner & Service Discovery
Scan a target host for open TCP ports within a user-specified range and identify common services running on those ports.

Web Crawler
Extract and list all hyperlinks from a user-provided webpage URL.

File Transfer
Client-server module to send and receive files over TCP sockets.

Wikipedia Data Fetcher
Fetch and display a summary paragraph for any topic using the Wikipedia REST API.

Network Device Scanner
Scan the local subnet (e.g., 192.168.1.1 - 192.168.1.254) to detect active devices.

Broadcast Messaging
Send and receive broadcast messages on the local network in real-time between instances of the application.

User Interface
A Tkinter-based GUI with a main menu to access each module.

Each tool runs independently when selected.

User inputs are validated with error handling.

Clear results displayed in the GUI.

Part B – Web-Based Real-Time Chat
Features
A simple HTTP server serving a static HTML page for the chat interface.

A WebSocket server managing real-time message broadcasting to all connected clients.

Messages sent by any client appear immediately on all other clients.

No external frameworks; implemented using Python’s built-in http.server, asyncio, and websockets modules.

Requirements
Python 3.x

Standard libraries: socket, threading, select, os, time, struct, asyncio, http.server

External libraries:

requests

beautifulsoup4

websockets

Cross-platform support: Windows, macOS, Linux

No third-party web frameworks (e.g., Flask, Django)

Installation & Setup
Clone the repository:   git clone https://github.com/burakshaus/network_toolkit.git 
                        cd network-tools-chat

Install required Python packages:  pip install requests beautifulsoup4 websockets // and other modules 

Run the GUI Network Toolkit: python main.py

Run the Web Chat Server:

Navigate to the chat server directory (e.g., partB/)

Run the HTTP and WebSocket server script:  python partBmain.py

Open your browser and access http://localhost:8000 (or the port specified) to use the chat interface.

Usage
Network Toolkit (GUI)
Launch main.py to open the toolkit window.

Select the desired tool from the main menu.

Follow on-screen instructions/input fields for each tool.

Use "Back to Main Menu" to switch between tools or exit.

Web-Based Chat
Start the chat server.

Open the browser to the server URL.

Type messages and see real-time updates from all connected users.

network-toolkit/
│
├── main.py                 # Main GUI toolkit launcher
├── port_scanner.py         # Port scanner module
├── web_crawler.py          # Web crawler module
├── file_transfer.py        # File transfer client/server modules
├── wiki_fetcher.py         # Wikipedia data fetcher module
├── network_scanner.py      # Network device scanner module
├── broadcast_messaging.py  # Broadcast messaging module
│
├── partB/            # Web chat server files
│   ├── http_server.py      # HTTP + WebSocket server script
|   |__ partBmain.py        # Main GUI toolkit launcher for Part B
│   └── index.html          # Static chat interface HTML file
│   |__ web_socket_server.py # The server broadcasts part B's chat message to all connected clients (including the sender)
└── README.md               # This file
