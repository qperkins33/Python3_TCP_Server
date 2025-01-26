# Import required modules
from socket import *
import sys  # For program termination
from datetime import datetime

# (Optional) To implement multithreading, the 'threading' module should be imported.
# import threading

def handle_request(connection_socket):
    """
    This function handles the client request. You need to fill in the blanks.
    """
    try:
        message = connection_socket.recv(1024).decode()

        # Extracts the filename from the given message.
        # For example, for "GET /HelloWorld.html HTTP/1.1" it extracts "HelloWorld.html".
        filename = message.split()[1][1:]

        with open(filename, 'r') as f:
            outputdata = f.read()

            # Send HTTP header with response
            # FILL IN start
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
            # FILL IN end

            for i in range(0, len(outputdata)):
                connection_socket.send(outputdata[i].encode())
            connection_socket.send("\r\n".encode())

    except IOError:
        # FILL IN start
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
        # FILL IN end
    finally:
        connection_socket.close()

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Bind to an address and port
    portnum = 12000

    # FILL IN start
    server_socket.bind(('localhost', portnum))
    # FILL IN end

    # Listen for incoming connections
    # FILL IN start
    server_socket.listen(1)
    # FILL IN end

    print("The server is ready to receive")

    while True:
        connection_socket, addr = server_socket.accept()

        # To implement a multithreaded server, you would create a new thread here
        # that runs the handle_request function. E.g.,
        # threading.Thread(target=handle_request, args=(connection_socket,)).start()

        # For now, just handle the request using the main thread
        handle_request(connection_socket)

    server_socket.close()
    sys.exit()  # Terminate the program

if __name__ == "__main__":
    main()
