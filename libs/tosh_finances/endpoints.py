from enum import Enum

class EndpointToshInterface:

    class HttpMethod(Enum):
        POST = 'post'
        GET = 'get'
        PUT = 'put'
        DELETE = 'delete'

    @classmethod
    def path(cls) -> str:
        raise NotImplementedError

    @classmethod
    def http_method(cls) -> HttpMethod:
        raise NotImplementedError