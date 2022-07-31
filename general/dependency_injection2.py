from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class Sample:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def parse(data: dict[str, str]):
        return Sample(
            data["a"], data["b"],
            data["c"], data["d"]
        )


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    sample = providers.Singleton(
        Sample.parse,
        config.data
    )


@inject
def main(sample: Sample = Provide[Container.sample]):
    print(sample.a, sample.b, sample.c, sample.d)


if __name__ == "__main__":
    cnt = Container()
    cnt.config.data.from_value({"a": 123, "b": 456, "c": 789, "d": 101112})
    cnt.wire(modules=[__name__])

    main()
