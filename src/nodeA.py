import threading
from shared import makePrimarySocket, recvMessages, sendMessages


socket = makePrimarySocket()

# create threads for listening and sending messages
threading.Thread(target=recvMessages, args=(socket,)).start()
threading.Thread(target=sendMessages, args=(socket,)).start()
