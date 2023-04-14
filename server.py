import socket
import time
import struct

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to a specific address and port
server_socket.bind(('147.46.132.224', 8881))

# Listen for incoming connections
server_socket.listen(1)

print('Waiting for incoming connections...')

# Accept incoming connections
client_socket, client_address = server_socket.accept()

print('Accepted connection from:', client_address)

# Read the frame sizes from the txt file
try:
    with open('frame_sizes.txt', 'r') as f:
        frame_sizes = f.read().splitlines()
except FileNotFoundError:
    print('Error: No frame_sizes.txt file found. Using default frame size of 80KB')
    frame_sizes = ['81920']

# Define the frame rate (in frames per second)
frame_rate = 30

# Define the duration of the video transmission (in seconds)
duration = 10

# Transmit the video frames
for i in range(frame_rate * duration):
    # Read the size of the next video frame from the txt file
    frame_size = int(frame_sizes[i % len(frame_sizes)])
    
    # Create a video frame of the specified size
    data = b'0' * frame_size

    # Pack the frame data and header into a message
    timestamp = struct.pack('d', float(time.time()))
    frame_size = struct.pack('L', frame_size)
    message = timestamp + frame_size  + data

    # Send the message to the client
    client_socket.sendall(message)

    print('Sent frame', i+1, 'of size', frame_size, 'to the client')
    
    # Wait for the next frame to be transmitted
    time.sleep(1/frame_rate)

# Close the connection
client_socket.close()
server_socket.close()