import socket
import time
import struct

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('147.46.132.224', 8881)
print('Connecting to %s:%s...' % server_address)
client_socket.connect(server_address)

# Receive the video frames from the server
while True:
    # Receive the message header from the server
    header_data = b''
    while len(header_data) < 16:
        chunk = client_socket.recv(16 - len(header_data))
        if not chunk:
            break
        header_data += chunk
    if len(header_data) < 16:
        break
    
    print('Header', len(header_data))
    # Unpack the timestamp and frame size fields from the message header
    timestamp, frame_size = struct.unpack('dL', header_data)
    
    # Receive the frame data from the server
    frame_data = b''
    while len(frame_data) < frame_size:
        chunk = client_socket.recv(frame_size - len(frame_data))
        if not chunk:
            break
        frame_data += chunk
    if len(frame_data) < frame_size:
        break
    
    # Print the timestamp and frame size
    print('Received frame with timestamp', timestamp, 'and size', frame_size)
    
# Close the connection
client_socket.close()