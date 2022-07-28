from PIL import Image, ImageDraw, ImageFont
import io


class TextToImageConverter:

    FONT = ImageFont.truetype(font="assets/monospace.ttf", size=20)
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
        return cls._transform_to_in_memory(img)

    @classmethod
    def _getSize(cls, txt, font):
        testImg = Image.new("RGB", (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)

    @classmethod
    def _transform_to_in_memory(cls, img):
        s = io.BytesIO()
        img.save(s, "png")
        return s.getvalue()
