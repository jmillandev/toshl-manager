BASE_URL = "https://api.toshl.com"  # TODO: Move this to a config file


class List:
    METHOD = "GET"
    URL = BASE_URL + "/categories"
    OPTIONAL_PARAMS = ["ids"]
