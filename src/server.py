from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Server(DatagramProtocol):

    def __init__(self):
        self.clients = dict()

    def datagramReceived(self, datagram: bytes, addr):
        datagram = datagram.decode("utf-8")
        if "ready" in datagram:

            # Parse datagram into ready&name&password
            try:
                ready, name, pw = datagram.split("&")
            except:
                self.transport.write("Please enter a username and password!".encode("utf-8"), addr)
                return

            # Check id name is already registered
            if name in self.clients.keys():
                data = self.clients.get(name) # Get array [password, IP]
                password = data[0]
                if password == pw: #Password matches
                    self.serverdata[name] = [pw, addr] # Add pw and IP to server datastore
                    addresses = "\n".join([str(x) + ": " + str(self.clients.get(x)[1]) for x in self.clients.keys()])
                    self.transport.write(addresses.encode("utf-8"), addr)
                else:
                    self.transport.write("Invalid Password for this username".encode("utf-8"), addr)
            # If name is not registered, add it
            else:
                self.serverdata[name] = [pw, addr]  # Add pw and IP to server datastore
                addresses = "\n".join([str(x) + ": " + str(self.clients.get(x)[1]) for x in self.clients.keys()])
                self.transport.write(addresses.encode("utf-8"), addr)

if __name__ == '__main__':
    reactor.listenUDP(9999, Server())
    reactor.run()