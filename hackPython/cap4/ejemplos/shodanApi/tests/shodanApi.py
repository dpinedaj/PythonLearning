import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from generalSearch import ShodanSearch


def test_length(text):
    """
    Function to verify the amount of hosts returned
    with a specific name or text    
    """
    sho = ShodanSearch()
    result = sho.search(text)

    print('total results:',result['total'])

def test_info_host(ip):
    """
    Function to verify the information about a host
    """
    sho = ShodanSearch()
    results = sho.info_host(ip)
    if results != None:
        for key, value in results.items():
            print(key, '-->', value)
    else:
        print('No results')

def test_search_ftp():
    """
    Function to search all the openned ftp ports without autenticacion
    """
    sites = list()
    sho = ShodanSearch()
    result = sho.search('port: 21 Anonymous user logged in')
    print('host number: ' + str(len(result['matches'])))
    for match in result['matches']:
        if match['ip_str'] is not None:
            print(match['ip_str'])
            sites.append(match['ip_str'])
    return sites

def bannerServer():
    """
    Function to see the exposed banners of a server.
    can show us if there's exposed something like the server's name
    the backend like python, java  versions.

    """
    import socket
    import argparse
    parser = argparse.ArgumentParser(description='Obtain banner server')
    parser.add_argument('-target', dest='target', help='target ip', required=True)
    parser.add_argument('-port', dest='port', help='port', type=int, required=True)
    parsed_args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((parsed_args.target, parsed_args.port))
    sock.settimeout(2)
    get = "GET / HTTP/1.1\nHost: {}\n\n".format(parsed_args.target)
    http_get = bytes(get, 'utf-8')
    data = " "
    try:
        sock.sendall(http_get)
        data = sock.recvfrom(1024)
        print(data)
    except socket.error:
        print("Socket error:", socket.errno)
    finally:
        print("Clossing connection")
        sock.close()


#test_length('google')

#test_info_host('8.8.8.8')
#test_search_ftp()
bannerServer()