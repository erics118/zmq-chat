import threading
from shared import makeSecondarySocket, recvMessages, sendMessages


socket = makeSecondarySocket()

# create threads for listening and sending messages
threading.Thread(target=recvMessages, args=(socket,)).start()
threading.Thread(target=sendMessages, args=(socket,)).start()
