import requests
import json


def pruebaGet():

    response = requests.get("http://httpbin.org/get?id=0123456789", timeout=5)

    print("Status Code: " + str(response.status_code))

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.request.headers.items():
            print(header, " ---> ", value)

        print("Server: " + response.headers["server"])

    else:
        print("Error code: " + str(response.status_code))


def pruebaPost():

    datos = {
        "id": "0123456789",
    }
    response = requests.post("http://httpbin.org/post", timeout=5, data=datos)

    print("Status Code: " + str(response.status_code))

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.request.headers.items():
            print(header, " ---> ", value)

        print("Server: " + response.headers["server"])

    else:
        print("Error code: " + str(response.status_code))


def pruebaHeaders():

    datos = {
        "id": "0123456789",
    }
    headers = {"user-agent": "my-user-agent-header/v1.0"}
    response = requests.post(
        "http://httpbin.org/post", timeout=5, data=datos, headers=headers
    )

    print("Status Code: " + str(response.status_code))

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.request.headers.items():
            print(header, " ---> ", value)

        print("Server: " + response.headers["server"])

    else:
        print("Error code: " + str(response.status_code))


def pruebaPatch():

    datos = {
        "id": "0123456789",
    }
    response = requests.patch("http://httpbin.org/patch", timeout=5, data=datos)

    print("Status Code: " + str(response.status_code))

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.request.headers.items():
            print(header, " ---> ", value)

        print("Server: " + response.headers["server"])

    else:
        print("Error code: " + str(response.status_code))


def pruebaPut():

    datos = {
        "id": "0123456789",
    }
    files = {
        "file": (
            "file.xlsx",
            open("file.xlsx", "rb"),
            "application/vnd.ms-excel",
            {"Expires": "0"},
        )
    }
    response = requests.put(
        "http://httpbin.org/patch", timeout=5, data=datos, files=files
    )

    print("Status Code: " + str(response.status_code))

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.request.headers.items():
            print(header, " ---> ", value)

        print("Server: " + response.headers["server"])

    else:
        print("Error code: " + str(response.status_code))
