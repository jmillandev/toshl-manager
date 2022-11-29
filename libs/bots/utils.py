class ScaperSpecialChars:
    """
    Clean a message scaping the special character so telegram can be process
    """

    ESCAPE_CHARS = (
        "_",
        "*",
        "[",
        "]",
        "(",
        ")",
        "~",
        "`",
        ">",
        "#",
        "+",
        "-",
        "=",
        "|",
        "{",
        "}",
        ".",
        "!",
    )

    @classmethod
    def clean(cls, message):
        for char in cls.ESCAPE_CHARS:
            message = message.replace(char, f"\{char}")
        return message
