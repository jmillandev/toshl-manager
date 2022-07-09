BASE_URL = "https://api.toshl.com"  # TODO: Move this to a config file


class List:
    METHOD = "GET"
    URL = BASE_URL + "/entries"
    OPTIONAL_PARAMS = ["type", "categories", "tags"]

class Update:
    METHOD = "PUT"
    URL = BASE_URL + "/entries/{id}"
    OPTIONAL_PARAMS = ["extra"]
