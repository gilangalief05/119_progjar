import sys
import socket
import logging
import threading


def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    while True:
        try:
            while True:
                # Send data
                message = input()
                message = message + '\r\n'
                if message == 'TIME\r\n' or message == 'QUIT\r\n':
                    sock.sendall(message.encode())
                    data = sock.recv(32).decode() + '\r\n'
                    print(data)
                if message == 'QUIT\r\n':
                    break
        finally:
            logging.warning("closed")
            sock.close()
            break


if __name__=='__main__':
    t = threading.Thread(target=kirim_data)
    t.start()
