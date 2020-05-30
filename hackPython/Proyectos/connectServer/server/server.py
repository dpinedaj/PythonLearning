import sys
import os
import socket
import time
import tqdm
import argparse


class Parameters:
    """Global parameters"""
    def __init__(self):
        self.description = """ Use Example: 
                + Pass the target and the port:
                    -T 127.0.0.1 -P 21
                + Pass the target and the port and the filename:
                    -T 127.0.0.1 -P 21 -F test.txt
                 """

        self.parser = argparse.ArgumentParser(description="socket connection",
                                 epilog=self.description,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

        self.__add_parameters()
        self.params = self.parser.parse_args().__dict__



    def __add_parameters(self):
        
        self.parser.add_argument('-T', '--target', metavar='target', dest='target',
                    help='target to scan', required=True)
        self.parser.add_argument('-P', '--port',dest='port',type=int, help='port to connect',
                            required=True)
        self.parser.add_argument('-F', '--file', dest='file', default=None,
                             help='Indicates that is a file transaction')
        self.parser.add_argument('-R', dest='receive', action='store_true', default=False,
                                help='Indicates if the code will receive a file')



class Server:

    def __init__(self, maxClient=1, **kwargs):
        self.ip = kwargs.get('target')
        self.port = kwargs.get('port')
        self.file = kwargs.get('file')
        self.R = kwargs.get('receive')

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen(maxClient)

        if self.R:
            self.receiveFile()
        
        elif self.file != None:
            self.sendFile(os.path.dirname(__file__), self.file)

        else:
            self.chat()

    def __close(self):
        try:
            self.conn.close()
            self.s.close()
        except:
            pass

    def __waitMsg(self, bufferSize=2048, enc='utf-8'):

        while True:
            try:
                data = self.conn.recv(bufferSize)
                if data and data != '':
                    print('Client :',data.decode(enc) )
            except KeyboardInterrupt:
                break

    def chat(self, bufferSize=2048, enc='utf-8'):
        print("Waiting for connections...")
        self.conn, self.adr = self.s.accept()
        print('Connected with: ', self.adr)
        while True:
            try:
                print("Waiting for messages:")
                self.__waitMsg()
                print("\n")
                
                msg = input("Enter your message: ").encode()
                self.conn.sendall(msg)
                
            except KeyboardInterrupt:
                self.__close()
                sys.exit()
            

    def receiveFile(self, path='.', sep='-', bufferSize=4096, enc='utf-8'):

        print("Waiting for connections...")
        try:
            self.conn, self.adr = self.s.accept()
            print('Connected with: ', self.adr)
            received = self.conn.recv(bufferSize).decode()

            fileName, fileSize = received.split(sep)
            fileSize = int(fileSize)

            if self.file != None:
                fileName = self.file
            fullPath = os.path.join(path, fileName)

            progress = tqdm.tqdm(range(fileSize), "Receiving {}".format(fileName), unit="B", unit_scale=True, unit_divisor=1024)
            with open(fullPath, "wb") as f:
                for _ in progress:
                    bytes_read = self.conn.recv(bufferSize)
                    if not bytes_read:
                        break
                    else:
                        f.write(bytes_read)
                    progress.update(len(bytes_read))
                    
            self.__close()
        except:
            self.__close()
            sys.exit()


    def sendFile(self, path, fileName, sep='-',bufferSize=4096, enc='utf-8'):

        print("Waiting for connections...")
        try:
            self.conn, self.adr = self.s.accept()
            print('Connected with: ', self.adr)

            fullPath = os.path.join(path, fileName)
            fileSize = os.path.getsize(fullPath)
            self.conn.send("{}{}{}".format(fileName, sep, fileSize).encode())

            progress = tqdm.tqdm(range(fileSize), "Sending {}".format(fileName), unit="B", unit_scale=True, unit_divisor=1024)

            with open(fullPath, "rb") as f:
                for _ in progress:

                    bytesRead = f.read(bufferSize)
                    if not bytesRead:
                        break
                    self.conn.send(bytesRead)

                    progress.update(len(bytesRead))
            self.__close()
        except:
            self.__close()
            sys.exit()

        


if __name__ == '__main__':

    params = Parameters()
    Server(**params.params)