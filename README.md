# EC500_P2P_Chat

| Collaborators               |
| --------------------------- |
| Ben Leone                   |
| Wiley Hunt                  |
| Noah Spahn                  |
| Purvis Amin                 |


## MVP

- Register yourself in the app to become discoverable to other users.
- Send a message to those you want to connect with to establish a session.
- For users who are offline, sending a message stores the message locally to be sent when other user comes online.
- All passwords and messages are hashed to be decrypted by other user.

## Setup

- Clone and `cd` into repository
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
- Run `python3 client.py` 
- Enter a name and password to register your IP with the central server (so you can discover and be discovered by others!)
- Enter the host IP and port number of other client and chat!

## Modules

- Server.py
    - Our remote server (hosted on GCP) which keeps track of users and IPs!
- Client.py
    - Our client application which enables a user to log-in, view other user IP's on the server, and engage in a Peer-to-Peer chat (over UDP). All messages are encrypted end-end!

## Technologies Used

- Application: Python (using the Twisted library)
- Database: SQLite (WIP)
- Encryption: PyCipher

## Bugs
- Currently, the first message is getting lost in the ether (never received). This may be something strange with the protocol, but needs further exploration.
- This is not currently working for 2 computers on the same local network

## References
- Our client.py and server.py are based on [this tutorial](https://www.youtube.com/watch?v=1Fay1pjttLg) using Twisted to create a P2P messaging system
