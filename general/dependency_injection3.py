from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from dataclasses import dataclass


@dataclass
class SampleData:
    a: int
    b: int
    c: int
    d: int


class Sample:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def parse(data: SampleData):
        return Sample(data.a, data.b, data.c, data.d)


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    sample = providers.Singleton(Sample.parse, config.data)


class Validator:
    @inject
    @staticmethod
    def main(sample: Sample = Provide[Container.sample]):
        print(sample.a, sample.b, sample.c, sample.d)


if __name__ == "__main__":
    sample_data = SampleData(123, 456, 789, 101112)
    cnt = Container()
    cnt.config.data.from_value(sample_data)
    cnt.wire(modules=[__name__])

    Validator.main()
    sample2 = Sample(1, 2, 3, 4)
    cnt.sample.override(sample2)
    Validator.main()
