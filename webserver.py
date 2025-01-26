# Import required modules
from socket import *
import sys  # For program termination
from datetime import datetime

def handle_request(connection_socket):
    """
    This function handles the client request. You need to fill in the blanks.
    """
    try:
        message = connection_socket.recv(1024).decode()

        # Extracts the filename from the given message.
        filename = message.split()[1][1:]

        with open(filename, 'r') as f:
            outputdata = f.read()

            # Send HTTP header with response
            current_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

            header = (
                "HTTP/1.1 200 OK\r\n"
                "Connection: close\r\n"
                f"Date: {current_date}\r\n"
                f"Content-Length: {len(outputdata)}\r\n"
                "Content-Type: text/html\r\n"
                "\r\n"
            )
            connection_socket.send(header.encode())

            for i in range(0, len(outputdata)):
                connection_socket.send(outputdata[i].encode())
            connection_socket.send("\r\n".encode())

    except IOError:
        current_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

        # Send HTTP 404 response when file not found
        error_body = "<html><body><h1>404 Not Found</h1></body></html>"

        error_header = (
            "HTTP/1.1 404 Not Found\r\n"
            "Connection: close\r\n"
            f"Date: {current_date}\r\n"
            f"Content-Length: {len(error_body)}\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
        )

        connection_socket.send(error_header.encode())
        connection_socket.send(error_body.encode())
    finally:
        connection_socket.close()

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Bind to an address and port
    portnum = 12000

    server_socket.bind(('localhost', portnum))

    # Listen for incoming connections
    server_socket.listen(1)

    print("The server is ready to receive")

    while True:
        connection_socket, addr = server_socket.accept()

        # Handle the request using the main thread
        handle_request(connection_socket)

    server_socket.close()
    sys.exit()  # Terminate the program

if __name__ == "__main__":
    main()
