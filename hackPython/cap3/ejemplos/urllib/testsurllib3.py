import urllib3
##------------------------DOCUMENTACION----------------
def reqPool():
    pool = urllib3.PoolManager(10)
    response = pool.request('GET', 'http://www.google.com')

def getProxy(proxy, puerto, url):
    direccionProxy = "http://{}:{}".format(proxy, puerto)

    proxy = urllib3.PoolManager(direccionProxy)

    response = proxy.request('GET', url)


#-----------------------EJEMPLOS----------------------------

def ejemploSinProxy(url):
    pool = urllib3.PoolManager(10)
    response = pool.request('GET', url)

    print(response.status)

    response.headers.keys()
    response.headers.values()

    for header, value in response.headers.items():
        print(header + " : " + value)


def ejemploConProxy(ip, puerto, url):
    pool = urllib3.PoolManager(10)
    direccionProxy = "http://{}:{}".format(ip, puerto)
    proxy = urllib3.ProxyManager(direccionProxy)
    response = proxy.request('GET',url)
    
    print(response.status)
    response.headers.keys()
    response.headers.values()

    for header, value in response.headers.items():
        print(header + " : " + value)

def ejemploConn(url, url2, url3):
    conn = urllib3.connection_from_url(url)
    r1 = conn.request('GET', url)
    r2 = conn.request('GET', url2)
    r3 = conn.request('GET', url3)
