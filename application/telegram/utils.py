from re import search


def parse_regex(message: str, regex_pattern: str)-> dict:
    matches = search(regex_pattern, message)
    if not matches:
        return {}

    return matches.groupdict()
