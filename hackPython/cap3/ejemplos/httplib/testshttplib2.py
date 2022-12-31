import httplib2


def prueba(url):
    h = httplib2.Http()
    response = h.request(url, "GET")
    response.geturl()
    response.getcode()
    response.headers.keys()
    response.headers.values()

    for header, value in response.headers.items():
        print(header + " : " + value)


prueba("http://www.google.com")
