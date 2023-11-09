import socket
import threading
import PySimpleGUI as psg

# Right column
log_column = [
    [psg.Button('Start')],
    [psg.Text("Log data:")],
    [psg.Text(size=(40, 15), key="-LOG OUTPUT-")],
]

# ----- Full layout -----
layout = [  
    [
        psg.Column(log_column),
    ]
]

# Create the window
window = psg.Window("TCP Server", layout)

BUFFER_SIZE = 64
TCP_PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, TCP_PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# when client connected, print which addr is connected to this server
# then get received message
def handle_client(conn, addr):
    try:
        print(f"[NEW CONNECTION] {addr} connected.")
        existingText = window['-LOG OUTPUT-']
        window['-LOG OUTPUT-'].update(existingText.get() + f"[NEW CONNECTION] {addr} connected." + "\n")
        connected = True
        while connected:
            msg_length = conn.recv(BUFFER_SIZE).decode(FORMAT)
            if msg_length:
                # check message length
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                # if client disconnect, close connection. 
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    #existingText = window['-LOG OUTPUT-']
                    #window['-LOG OUTPUT-'].update(existingText.get() + msg + "\n")
                    break
                print(f"[{addr}] {msg}")
                existingText = window['-LOG OUTPUT-']
                window['-LOG OUTPUT-'].update(existingText.get() + f"[{addr}] {msg}" + "\n")
                conn.send("Server sent - Msg received!".encode(FORMAT))
    finally:
        conn.close()

# server starts listening
# start multithread and check number of active threads
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == psg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Start':
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            existingText = window['-LOG OUTPUT-']
            window['-LOG OUTPUT-'].update(existingText.get() + f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}" + "\n")


start()