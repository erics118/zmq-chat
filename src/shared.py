import zmq


def recvMessages(socket):
    """Receive messages from the socket."""

    while True:
        message = socket.recv().decode("utf-8")
        print("Received message: ", message)


def sendMessages(socket):
    """Send messages to the socket."""
    while True:
        msg = input("Enter your message: ")
        socket.send(msg.encode("utf-8"))


def makeSocket():
    """Create a socket."""

    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    return socket


def makePrimarySocket():
    """Create a socket and bind it to a port."""

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"A")
    socket.bind("tcp://*:5555")
    return socket


def makeSecondarySocket():
    """Create a socket and connect it to a port."""

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"B")
    socket.connect("tcp://localhost:5555")
    return socket
