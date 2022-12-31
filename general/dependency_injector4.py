from dataclasses import dataclass

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


@dataclass
class TestModel:
    a: int
    b: int
    c: int

    @staticmethod
    def parse(data):
        return TestModel(a=data["a"], b=data["b"], c=data["c"])


class Container1(containers.DeclarativeContainer):
    config = providers.Configuration()
