#!/usr/local/bin/python3
import socketserver, argparse

p = argparse.ArgumentParser(description='Simple server program to send/receive messages,\n'
                                        'only 100 messages can be in queue.')
p.add_argument('-p', '--port', type=int, help='PORT number')

# message container

messages = [None for i in range(10001)]
counter = 0


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        def get(q):
            global counter

            index_m = [i for i in range(len(messages)) if messages[i]]
            # print(index_m)
            if len(index_m):
                if int(q) in index_m:
                    d = messages[int(q)]
                    messages[int(q)] = None
                    counter -= 1
                    return bytes(d + '\n[done]', 'utf-8')
                x = min(index_m)
                d = messages[x]
                messages[x] = None
                counter -= 1
                return bytes(d + '\n[done]', 'utf-8')

        def post(q, po):
            global counter
            index_n = [i for i in range(len(messages)) if not messages[i]]
            # print(index_n[9980:])
            if counter < 100:
                messages.insert(int(q), po)
                messages.pop(max(index_n))
                counter += 1
                return bytes('[done]', 'utf-8')

        self.data = str(self.request.recv(1024), 'utf-8').split('|||')
        print(self.data)
        if len(self.data) == 1:
            self.data = get(self.data[0])
            self.request.sendall(self.data) if self.data else None
        if len(self.data) == 2:
            self.data = post(self.data[1], self.data[0])
            self.request.sendall(self.data) if self.data else None


if __name__ == '__main__':

    if not p.parse_args().port:
        p.print_help()
        exit()
    HOST, PORT = 'localhost', p.parse_args().port
    s = socketserver.TCPServer((HOST, PORT), MyHandler)
    print("server is up", PORT)
    s.serve_forever()