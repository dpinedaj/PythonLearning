import urllib


def prueba():
    proxies = {"http": "http://<direccion_ip>:<Puerto>"}

    print("Using HTTP proxy %s" % proxies["http"])

    response = urllib.urlopen("http://www.google.com", proxies=proxies)
    response.geturl()
    response.getcode()
    response.headers.keys()
    response.headers.values()

    for header, value in response.headers.items():
        print(header + ":" + value)


prueba()
