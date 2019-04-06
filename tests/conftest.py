import socket


def server_test(host, port):

    args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    for family, socktype, proto, canonname, sockaddr in args:
        s = socket.socket(family, socktype, proto)
        try:
            s.connect(sockaddr)
        except socket.error:
            return False
        else:
            s.close()
            return True


collect_ignore = []
if not server_test('localhost', 8443):
    collect_ignore_glob = ['integration/*.py']