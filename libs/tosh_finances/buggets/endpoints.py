from ..endpoints import EndpointToshInterface


class List(EndpointToshInterface):

    @classmethod
    def http_method(cls) -> EndpointToshInterface.HttpMethod:
        return cls.HttpMethod.GET

    @classmethod
    def path(cls) -> str:
        return "/budgets"
