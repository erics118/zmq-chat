import argparse
import threading
from ip import encodeIp

from shared import makePrimarySocket, makeSecondarySocket, recvMessages, sendMessages


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--primary", action="store_true")
group.add_argument("--secondary", action="store_true")
parser.add_argument("--code", type=str, required=False)

args = parser.parse_args()

if args.primary:
    socket, ip = makePrimarySocket()

if args.secondary:
    socket, ip = makeSecondarySocket(args.code)

print(f"IP Address: {ip}\nRoom Code: {encodeIp(ip)}\n-------------------")

# create threads for listening and sending messages
threading.Thread(target=recvMessages, args=(socket,)).start()
threading.Thread(target=sendMessages, args=(socket,)).start()
