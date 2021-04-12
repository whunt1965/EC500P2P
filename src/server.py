from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

serverdata = dict()

class Server(DatagramProtocol):

    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram: bytes, addr):
        datagram = datagram.decode("utf-8")
        if "ready" in datagram:
            try:
                ready, name, pw = datagram.split("&")
                password = serverdata.get(name)
            except:
                self.transport.write("Please enter a username and password!".encode("utf-8"), addr)
                return
            if password == None or password == pw:
                serverdata[name] = pw
                addresses = "\n".join([str(x) for x in self.clients])
                self.transport.write(addresses.encode("utf-8"), addr)
                self.clients.add(name + str(addr))
            else:
                self.transport.write("Invalid Password!".encode("utf-8"), addr)

if __name__ == '__main__':
    reactor.listenUDP(9999, Server())
    reactor.run()