import zmq

from ip import decodeIp, getIpAddress


def recvMessages(socket, stopEvent):
    """Receive messages from the socket."""

    while not stopEvent.is_set():
        try:
            msg = socket.recv_string(flags=zmq.NOBLOCK)
            command = msg.split(" ")[0]

            match command:
                case "PING":
                    socket.send_string("PONG")
                case "CONNECTED":
                    print("! A secondary node has connected to this primary.")
                    socket.send_string("ACK-CONNECTED")
                case "ACK-CONNECTED":
                    print("! Connected to a primary node.")
                case "DISCONNECTED":
                    print("! Another node has disconnected from this node.")
                    stopEvent.set()
                    socket.close()
                case _:
                    print(">", msg)
        except zmq.Again:
            continue


def sendMessages(socket, stopEvent):
    """Send messages to the socket."""

    while not stopEvent.is_set():
        msg = input("")
        # need this check bc input() doesn't check it
        if stopEvent.is_set():
            break
        socket.send_string(msg)
        if msg == "EXIT":
            print("! Exiting...")
            socket.send("DISCONNECTED".encode("utf-8"))
            stopEvent.set()
            socket.close()
            break


def makeSocket():
    """Create a socket."""

    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    return socket


def makePrimarySocket():
    """Create a socket and bind it to a port."""

    ip = getIpAddress()

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"A")
    socket.bind("tcp://*:5555")
    return (socket, ip)


def makeSecondarySocket(code):
    """Create a socket and connect it to a port."""

    ip = decodeIp(code)

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"B")
    socket.connect(f"tcp://{ip}:5555")
    socket.send("CONNECTED".encode("utf-8"))
    return (socket, ip)
