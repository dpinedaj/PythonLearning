# Python2.7
import httplib


def prueba():
    h = httplib.HTTP("www.cwi.nl")
    h.putrequest("GET", "/index.html")
    h.putheader("Accept", "text/html")
    h.putheader("Accept", "text/plain")
    h.endheaders()

    errcode, errmsg, headers = h.getreply()

    print(errcode)
    f = h.getfile()
    data = f.read()
    print(data)
    f.close()


prueba()
