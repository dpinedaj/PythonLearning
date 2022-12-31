"""
Realiza un Script en Python en el que se implemente la clase cuentaBancaria.
Como mínimo debe contener los siguientes atributos: titular, número de cuenta y saldo
Como mínimo debe tener métodos que permitan hacer ingresos, retirar una cantidad de dinero, consultar el saldo y movimientos de la cuenta.
En el mismo script escribe un ejemplo práctico usando los diferentes métodos para comprobar el funcionamiento de la clase, el cual debe ser coherente,
 si el saldo es cero, no se podrá retirar dinero de la cuenta.
"""


class cuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.mvtos = 0

    def ingresar(self, valor):
        valorEjecucion = None

        try:
            self.saldo = self.saldo + valor
            valorEjecucion = "OK"
            self.mvtos += 1
        except:
            valorEjecucion = "ERROR"
        return valorEjecucion

    def retirar(self, valor):
        valorEjecucion = None
        try:
            valorFinal = self.saldo - valor
            if valorFinal >= 0:
                self.saldo = valorFinal
                valorEjecucion = "OK"
                self.mvtos += 1
            else:
                valorEjecucion = "SIN_SALDO"
        except:
            valorEjecucion = "ERROR"
        return valorEjecucion

    def consultar_saldo(self):
        self.mvtos += 1
        return self.saldo

    def consultar_mvtos(self):
        return self.mvtos

    def __repr__(self):
        return """Cuenta bancaria,
                titular: {},
                numero_cuenta: {},
                saldo: {},
                mvtos: {}""".format(
            self.titular, self.numero_cuenta, self.saldo, self.mvtos
        )
