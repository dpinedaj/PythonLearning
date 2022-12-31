import requests


def prueba1():
    url = input("enter a website to extract url's from: ")
    r = requests.get(url)
    print(r.status_code)
    print(r.url)
    print(r.text)


def prueba2():
    response = requests.get("http://www.google.com")
    print(response.status_code)  # 200
    print(response.headers)
    print(response.url)  # google.es.... --> Se puede ver que fue redireccionado.
    print(response.history)  # 302 debido al redireccionamiento


def prueba3():
    response = requests.get(
        "http://www.google.com", allow_redirects=False
    )  # Se desactivan las redirecciones.
    print(response.url)  # En este caso el url es el mismo del request.
    print(response.status_code)  # En este caso aparece directamente 302
    print(response.history)  # Se muestra vacío ya que no hubieron redirecciones


def pruebaJson():
    print("Requests usando json")

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?&q=london&appid=0888d6d73eeb6588a5b5da08f4d32bb9",
        timeout=5,
    )

    print("status code: ", str(response.status_code))
    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.headers.items():
            print(header + " --> " + value)

        print("Headers request: ")
        for header, value in response.request.headers.items():
            print(header + " --> " + value)

    else:
        print("Error code %s" % response.status_code)


def pruebaPost():
    data = {"id": "0123456789", "email": "prueba@pŕueba.com"}

    header = {"Content-Type": "application/json", "Accept": "application/json"}

    cookies = {"cookies_1": "una cookie evitada"}

    url = "http://example.com/api/alta_usuario"
    response = requests.post(url, data=data, headers=header, cookies=cookies)


pruebaJson()
