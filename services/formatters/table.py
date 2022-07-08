from .interface import RenderInterface
from .utils import format_values_to_str

CORNER = '+'
V_LINE = '|'
H_LINE = '-'

class TableFormat(RenderInterface):

  def execute(self, data: tuple) -> str:
    if len(data) == 0:
      return 'Empty Data'
    data = tuple(map(format_values_to_str, data))

    headers = data[0].keys()
    columns_width = self._columns_width(data).values()
    line_break = self._line_break(columns_width)
    response = line_break
    response += self._line_with_data(headers, columns_width)
    response += line_break
    for row in data:
      response += self._line_with_data(row.values(), columns_width)
    response += line_break
    return response

  def _columns_width(self, data):
    headers = data[0].keys()
    columns_width = { header: len(header) for header in headers }
    for row in data:
      for header in headers:
        value = row.get(header, '')
        columns_width[header] = max(columns_width[header], len(value))
    return columns_width

  def _line_break(self, columns_width):
    line = CORNER
    for width in columns_width:
      line += (H_LINE * (width + 2)) + CORNER
    return line + '\n'

  def _line_with_data(self, values, columns_width):
    line = V_LINE
    columns_width = tuple(columns_width)
    for i, value in enumerate(values):
      width = columns_width[i]
      line += ' {:^{width}} {}'.format(value, V_LINE, width=width)
    return line + '\n'
