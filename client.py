#!/usr/local/bin/python3
import socket, argparse

host = "localhost"

p = argparse.ArgumentParser(description='Simple program for sending/receiving messages, with assigning\n'
										'number of queue.')
p.add_argument('-P', '--PORT', type=int, help='Please enter valid port. port must be 0-65535')
p.add_argument('-p', '--post', help='Enter message to store/update on server, type [--queue] and digit after message\n'
                                    'to assignqueue number')
p.add_argument('-g', '--get', action='store_true', help='Get messages')
p.add_argument('-q', '--queue', help='Queue number. Can be from 0 to 10000.')


def client(port, g=False, po=None, q=None):
    post = lambda x, y: bytes(x + '|||' + y, 'utf-8')
    get = lambda x: bytes(x, 'utf-8')

    if not q:
        q = '0'

    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if g and (int(q) in range(10001)):
            con.connect((host, port))
            data = get(q)
            con.send(data)
            recv = str(con.recv(1024), "utf-8")
            print(recv)
            con.close()
            return recv

        if po and (int(q) in range(10001)) and not '|||' in po:
            con.connect((host, port))
            data = post(po, q)
            con.send(data)
            recv = str(con.recv(1024), "utf-8")
            print(recv)
            con.close()
            return recv
        return p.print_help()
    except:
        p.print_help()


if __name__ == '__main__':
    client(p.parse_args().PORT, p.parse_args().get, p.parse_args().post, p.parse_args().queue)