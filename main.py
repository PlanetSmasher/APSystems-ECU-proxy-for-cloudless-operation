import socketserver
from socketserver import BaseRequestHandler
from datetime import datetime, timedelta
import threading


host = '172.16.x.x' #Your host IP-address here


class HTTPSERVER(BaseRequestHandler):
    def handle(self):
        rec = self.request.recv(1024)
        if rec:
            try:
                date_time_obj = datetime.strptime(str(rec)[62:76], '%Y%m%d%H%M%S') + timedelta(minutes=-5)
                send_str = '101' + datetime.strftime(date_time_obj, '%Y%m%d%H%M%S')
            except:
                send_str = '100'  # all is fine ;)
            finally:
                self.request.send(send_str.encode('utf-8'))

listener_1 = socketserver.TCPServer((host, 8995), HTTPSERVER)
thread_1 = threading.Thread(target=listener_1.serve_forever)
listener_2 = socketserver.TCPServer((host, 8996), HTTPSERVER)
thread_2 = threading.Thread(target=listener_2.serve_forever)
for threads in thread_1, thread_2:
    threads.start()

for threads in thread_1, thread_2:
    threads.join()
