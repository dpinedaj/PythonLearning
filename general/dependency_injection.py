from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

import os
from unittest import mock


class ApiClientDep:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")  # <-- dependency issue
        self.timeout = os.getenv("TIMEOUT")  # <-- dependency issue


class ApiClient:
    def __init__(self, api_key: str, timeout: int):
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


class Service:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client  # <-- dependency is injected


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )


@inject
def main(service: Service = Provide[Container.service]):
    ...


if __name__ == "__main__":
    container = Container()
    container.config.api_key.from_env("API_KEY", required=True)
    container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()  # <-- dependency is injected automatically

    with container.api_client.override(mock.Mock()):
        main()  # <-- overridden dependency is injected automatically


################################################################


class Photo:
    ...


class User:
    def __init__(self, uid: int, main_photo: Photo) -> None:
        self.uid = uid
        self.main_photo = main_photo


class Container(containers.DeclarativeContainer):

    photo_factory = providers.Factory(Photo)

    user_factory = providers.Factory(
        User,
        main_photo=photo_factory,
    )


if __name__ == "__main__":
    container = Container()

    user1 = container.user_factory(1)
    # Same as: # user1 = User(1, main_photo=Photo())

    user2 = container.user_factory(2)
    # Same as: # user2 = User(2, main_photo=Photo())

    another_photo = Photo()
    user3 = container.user_factory(
        uid=3,
        main_photo=another_photo,
    )
    # Same as: # user3 = User(uid=3, main_photo=another_photo)
