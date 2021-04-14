## EC500P2P

#P2P Chat Hackathon - 



#Summary: 
During this class activity, we attempted to build a chat app that securely utilized chat messages between parties without routing the news through a server. The P2P security requirement is accomplished through a python based p2p chat client app and a google hosted server that enables the discovery of others using the chat app. We were also encouraged to store messages to allow for que triggering if one party was not online. We struggle to implement local storage of messages, and while the app has a local database, it does not correctly store messages and ID to be queried later. During session initiation, a user will connect and join, but we only have successful testing with a single two parties connected rather than a multithreaded chat app. The user does, however, like in the documentation, initiate a conversation with a message from a user. We did initiate some hashing but given the database wasn't fully implemented, security hashing can mostly see these in the assignment of unique ids and unique conversation tags. In the future, we hope to complete more of the synchronization step and implement a GUI that is more pleasant than a console.  

#Acknowledgments: 
In this project, we used a video reference and twisted python libraries. The database work was based in sqlite3. 

https://www.youtube.com/watch?v=1Fay1pjttLg