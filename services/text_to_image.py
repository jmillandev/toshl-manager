from PIL import Image, ImageDraw, ImageFont


class TextToImageConverter:

    FONT = ImageFont.truetype(font="assets/monospace.ttf", size=17)
    COLOR_TEXT = "black"
    COLOR_BACKGROUND = "white"
    MARGIN = 2

    @classmethod
    def execute(cls, text) -> str:
        width, height = cls._getSize(text, cls.FONT)
        img = Image.new(
            "RGB",
            (width + cls.MARGIN * 2, height + cls.MARGIN * 2),
            cls.COLOR_BACKGROUND,
        )
        d = ImageDraw.Draw(img)
        d.text((cls.MARGIN, cls.MARGIN), text, fill=cls.COLOR_TEXT, font=cls.FONT)

        img.save("image.png")

    @classmethod
    def _getSize(cls, txt, font):
        testImg = Image.new("RGB", (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)
