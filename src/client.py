from uuid import uuid4

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
import sqlite3

# create connection
conn = sqlite3.connect('chatlog.db')  # used to generate db file

# create cursor
c = conn.cursor()  # used to create tables
# creating table
c.execute("""CREATE TABLE chat (
    user_name TEXT,
    user_ID INTEGER,
    messeges TEXT,
    msgcount INTEGER,
    localattachment BLOB

)""")


def localbd():
    c.execute("INSERT INTO chat VALUES()")


# conn.close() #best practice to close connection


class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == "localhost":
            host = "127.0.0.1"

        self.id = host, port
        self.address = None #The other client we talk to
        self.server = '', 9999 # Ask Wiley for the IP
        print("Working on id:", self.id)

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.server)
        # self.transport.write("ready".encode("utf-8"), self.address)

    def datagramReceived(self, datagram: bytes, addr):
        datagram = datagram.decode('utf-8')

        if addr == self.server:
            print("Choose a client from this list\n", datagram)
            self.address = input("Choose Host: "), int(input("Choose Port: "))

            # Allows us to refresh and view entire IP list
            if self.address == ('', 0):
                self.transport.write("ready".encode("utf-8"), self.server)
            else:
                reactor.callInThread(self.send_message)

        else:
            print(addr, ":", datagram)

        print(self.address)

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)

if __name__ == '__main__':
    # IP = input("Enter Your IP: ")
    port = randint(1000, 5000) # We should stabilize this port for impl
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()