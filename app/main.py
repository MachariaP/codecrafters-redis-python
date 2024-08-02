#!/usr/bin/env python3
import socket

def main():
    print("Logs from your program will appear here!")

    try:
        # Create a server socket
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        print("Server started on localhost:6379")
    except Exception as e:
        print(f"Failed to start server: {e}")
        return

    while True:
        try:
            print("Waiting for a client to connect...")
            client_socket, client_address = server_socket.accept() # wait for client
            print(f"Connected to client at {client_address[0]}:{client_address[1]}")

            # Send the PING response
            response = "+PONG\r\n"
            client_socket.sendall(response.encode('utf-8'))
            print("Sent response: +PONG")

            # Close the client connection
            client_socket.close()
            print(f"Closed connection from {client_address}")
        except Exception as e:
            print(f"Error handling client: {e}")

if __name__ == "__main__":
    main()
