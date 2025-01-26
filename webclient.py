# Import required modules
from socket import *
import sys  # For program termination

def main():

    if len(sys.argv) != 4:
        print("The command format is: webclient.py <server_host> <server_port> <filename>")
        sys.exit()

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        clientSocket.connect((server_host, server_port))
        print(f"Connected to server.\nServer Host: {server_host}\nServer Port: {server_port}\nFile Name: {filename}\n")

        response_message = f"GET /{filename} HTTP/1.1 \r\nHost: {server_host}\r\n\r\n"
        clientSocket.send(response_message.encode())

        # Receive response
        response = b""
        while True:
            response_part = clientSocket.recv(1024)  # Keep receiving in chunks of 1024 bytes
            if not response_part:  # Break if no more data is received
                break
            response += response_part

        print(f"Sever Response: {response.decode()}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        clientSocket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
