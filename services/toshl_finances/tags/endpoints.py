BASE_URL = "https://api.toshl.com"  # TODO: Move this to a config file


class List:
    METHOD = "GET"
    URL = BASE_URL + "/tags"
    OPTIONAL_PARAMS = ["ids"]
