import threading
import time
import datetime

class live_time(threading.Thread):
    def run(self):
        while True:
           waktu = datetime.datetime.now()
           buffer = waktu.strftime("%f")
           buffer = buffer[:1]
           if buffer == '0':
               jam = waktu.strftime("%X")
               print("JAM {}\r\n".format(jam))
               time.sleep(0.1)

def main():
    time = live_time()
    time.daemon = True
    time.start()


if __name__ == "__main__":
    try:
      main()
      while True:
        pass
    except KeyboardInterrupt:
      print('Program terminated')
