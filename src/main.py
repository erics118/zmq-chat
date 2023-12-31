import threading
from args import parseArgs
from ip import encodeIp

from shared import makePrimarySocket, makeSecondarySocket, recvMessages, sendMessages

args = parseArgs()

if args.primary:
    socket, ip = makePrimarySocket()

if args.secondary:
    socket, ip = makeSecondarySocket(args.code)

print(f"IP Address: {ip}\nRoom Code: {encodeIp(ip)}\n-------------------")

stopEvent = threading.Event()

# create threads for listening and sending messages
threading.Thread(target=recvMessages, args=(socket, stopEvent)).start()
threading.Thread(target=sendMessages, args=(socket, stopEvent)).start()
