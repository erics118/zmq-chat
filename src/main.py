import argparse
import threading

from shared import makePrimarySocket, makeSecondarySocket, recvMessages, sendMessages


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--primary", action="store_true")
group.add_argument("--secondary", action="store_true")
parser.add_argument("ip", type=str)

args = parser.parse_args()

if args.primary:
    socket = makePrimarySocket(args.ip)

if args.secondary:
    socket = makeSecondarySocket(args.ip)

# create threads for listening and sending messages
threading.Thread(target=recvMessages, args=(socket,)).start()
threading.Thread(target=sendMessages, args=(socket,)).start()
