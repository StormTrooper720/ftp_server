from pyftpdlib.handlers import *
from pyftpdlib.servers import *
from pyftpdlib.authorizers import *



def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user1', '12345', './files/user1', perm='elradfmwMT')
    authorizer.add_anonymous('./files/anonymous', perm='elr')

    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = 100 * 1024 * 1024 * 1024  # 100 Gb/sec
    dtp_handler.write_limit = 100 * 1024 * 1024 * 1024  # 100 Gb/sec

    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
    ftp_handler.dtp_handler = dtp_handler

    server = FTPServer(('192.168.4.84', 21), ftp_handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
