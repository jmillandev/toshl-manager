from libs.formatters.utils import format_values_to_str

from .interface import RenderInterface


class CsvFormat(RenderInterface):
    def format(self, data: tuple) -> str:
        if len(data) == 0:
            return "Empty Data"
        data = tuple(map(format_values_to_str, data))

        headers = data[0].keys()
        response = self._line_with_data(headers)
        for row in data:
            response += self._line_with_data(row.values())
        return response

    def _line_with_data(self, values):
        return ",".join(values) + "\n"
