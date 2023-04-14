# Video Transmission via Python Socket

This is a set of Python scripts that transmit emulated video frames from a server to a client via a Python socket. The client-side script receives the video frames, and the server-side script sends the video frames.

## Prerequisites

To run these scripts, you'll need:

- Python 3.x installed on your machine
- Basic knowledge of Python and networking concepts
- Access to a server and a client that can communicate with each other via a Python socket

## Installation

1. Clone this repository to your local machine.
2. Open the `client.py` and `server.py` files in your favorite text editor or IDE.
3. Modify the `server_address` variable in the `client.py` file to match your server's IP address and port number.
4. Modify the IP address and port number in the `server_socket.bind()` function in the `server.py` file to match your server's IP address and port number.
5. Modify the `frame_sizes` variable in the `server.py` file to match the desired frame sizes for the video transmission. You can also create a `frame_sizes.txt` file in the same directory as the `server.py` file and list the frame sizes in separate lines.
6. Save the modified files.

## Usage

### Server-side

1. Open a terminal window and navigate to the directory where the `server.py` file is stored.
2. Run the `server.py` file by typing `python server.py` in the terminal.
3. The server will start listening for incoming connections from a client.
4. Once a connection is established, the server will start transmitting emulated video frames to the client.
5. The server will print the size of each transmitted frame to the console.

### Client-side

1. Open a terminal window and navigate to the directory where the `client.py` file is stored.
2. Run the `client.py` file by typing `python client.py` in the terminal.
3. The client will connect to the server and start receiving emulated video frames.
4. Once a frame is received, the client will print the timestamp and frame size to the console.

## Contributing

If you find a bug or have an idea for a new feature, feel free to contribute to this project by submitting a pull request.

## Acknowledgments

These scripts were inspired by the following resources:

- Python Socket Programming Tutorial by Real Python: https://realpython.com/python-sockets/
