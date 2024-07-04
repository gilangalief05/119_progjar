import sys
import socket
import logging
import threading


def kirim_data(nama="kosong"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.16.16.101', 8889)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    while True:
        try:
            while True:
                message = input()
                message = message + '\r\n'
                if message == 'QUIT\r\n':
                    break
                sock.sendall(message.encode())
                data = sock.recv(32).decode() + '\r\n'
                print(data)
        finally:
            logging.warning("closed")
        return


if __name__=='__main__':
    threads = []
    for i in range(1):
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()
