#!/usr/local/bin/python3
import socket, argparse, sys

HOST = "localhost"

p = argparse.ArgumentParser(description='Simple program for\n'
										'sending/receiving\n'
										'messages, with assigning\n'
										'number of queue.')
p.add_argument('-P', '--PORT', type=int, help='Please enter valid port.')
p.add_argument('-p', '--post', help='Enter message to\n'
									'store/update on server, type [--queue]\n'
									'and digit after message to assign\n'
									'queue number')
p.add_argument('-g', '--get', action='store_true', help='To get a specific\n'
														'message,\n'
														'type [--queue]\n'
														'and enter the\n'
														'corresponding number')
p.add_argument('-q', '--queue', help='Queue number. Can be from 0 to 10000.')


def client(port, ge=False, po=None, qu=None):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	get = 'get' if ge else False
	post = 'post:' + po if po else False
	if qu and int(qu) not in range(10001):
		p.print_help()
		return
	queue = ':' + qu if qu else False
	data = ''.join([i for i in (get, post, queue) if type(i) == str])

	if data:
		con.connect((HOST, port))
		con.send(bytes(data, "utf-8"))
		r = str(con.recv(1024), "utf-8")
		print(r)
		con.close()
		return r


if __name__ == '__main__':
	if len(sys.argv[:]) < 2:
		p.print_help()
		exit()

	client(p.parse_args().PORT, p.parse_args().get, p.parse_args().post, p.parse_args().queue)
