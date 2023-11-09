import socket
import PySimpleGUI as psg

# Left column
tcp_config_column = [
    [psg.Text("Server IP and PORT")],
    [psg.Input(key='-SERVER IP-')],
    [psg.Input(key='-SERVER PORT-')],
    [psg.Button('Connect')],
    [psg.Text("Message to send")],
    [psg.Input(key='-INPUT-')],
    [psg.Button('Send'), psg.Button('Quit')],
]

# Right column
log_column = [
    [psg.Text("Log data:")],
    [psg.Text(size=(40, 5), key="-LOG OUTPUT-")],
]

# ----- Full layout -----
layout = [  
    [
        psg.Column(tcp_config_column),
        psg.VSeperator(),
        psg.Column(log_column),
    ]
]

# Create the window
window = psg.Window("TCP Client", layout)

BUFFER_SIZE = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # byte representation of string
    send_length += b' ' * (BUFFER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    received_message = client.recv(2048).decode(FORMAT)
    existingText = window['-LOG OUTPUT-']
    window['-LOG OUTPUT-'].update(existingText.get() + received_message + "\n")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == psg.WINDOW_CLOSED or event == 'Quit':
        client.close()
        break

    if event == "Connect":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (values['-SERVER IP-'], int(values['-SERVER PORT-']))
        client.connect(ADDR)
        pass

    if event == "Send":
        send(values['-INPUT-'])
        
# Finish up by removing from the screen
window.close()