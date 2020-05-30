import sys
import argparse
import socket

class Parameters:
    """Global parameters"""
    def __init__(self):
        self.description = """ Use Example: 
                + Basic Scan:
                    -T 127.0.0.1
                + Pass a specific port:
                    -T 127.0.0.1 -P 21
                + Pass a specific port range:
                    -T 127.0.0.1 -P 1 65000
                + Just show openned ports:
                    -T 127.0.0.1 -O """

        self.parser = argparse.ArgumentParser(description="port_scanning",
                                 epilog=self.description,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

        self.__add_parameters()
        self.params = self.parser.parse_args().__dict__


    def __add_parameters(self):
        
        self.parser.add_argument('-T', '--target', metavar='target', dest='target',
                    help='target to scan', required=True)
        self.parser.add_argument('-P', '--port',dest='ports',nargs='*',type=int, help='port to scan. Default 80',
                            default=80)
        self.parser.add_argument('-v', dest='verbose', default=0, action='count', help='verbosity level -v, -vv, -vvv')

        self.parser.add_argument('-O', '--open', dest='only_open', action='store_true', help='only display open ports',
                            default=False)

        
class Scanner:

    def __init__(self, **kwargs):

        self.ip = kwargs.get('target')
        self.ports = kwargs.get('ports')
        self.o = kwargs.get('only_open')

    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = s.connect_ex((self.ip, port))
            if conn == 0:
                returnValue = True
            else:
                returnValue = False
            s.close()
        
        except KeyboardInterrupt:
            sys.exit()
        except:
            returnValue = False
        
        return returnValue

    def get_ports(self):

        openPorts = list()
        if len(self.ports) > 1:
            mi = min(self.ports)
            ma = max(self.ports)
            for port in range(mi, ma+1):
                if self.scan_port(port):
                    openPorts.append(port)
            
        else:
            if self.scan_port(self.ports[0]):
                openPorts.append(self.ports[0])
        
        return openPorts

params = Parameters()
scanner = Scanner(**params.params)
print(scanner.get_ports())





