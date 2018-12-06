from server import server
from GameBoardShowCase import show_case_client
from client import client, client_ai
import threading
from time import sleep


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        # run server
        server.run()


class ShowCaseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        # run show_case
        show_case_client.run()


class ClientAiThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        # run ai player
        client_ai.run()
        

class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        # run random player
        client.run()

lock = threading.Lock()
serverT = ServerThread()
show_caseT = ShowCaseThread()
client_aiT = ClientAiThread()
clientT = ClientThread()

serverT.start()
sleep(1)

show_caseT.start()
sleep(1)

client_aiT.start()
clientT.start()
