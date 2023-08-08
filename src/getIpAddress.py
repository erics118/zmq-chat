import socket


def getIpAddress():
    """Get the IP address of the current machine."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # doesn't have to be reachable
        sock.connect(("10.1.1.1", 1))
        ip = sock.getsockname()[0]
    except socket.error:
        ip = "0.0.0.0"
    finally:
        sock.close()

    return ip
