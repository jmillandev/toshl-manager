from .interface import RenderInterface

class CsvFormat(RenderInterface):

  def exec(self, data: tuple) -> str:
    if len(data) == 0:
      return 'Empty Data'

    headers = data[0].keys()
    response = self._line_with_data(headers)
    for row in data:
      response += self._line_with_data(row.values())
    return response

  def _line_with_data(self, values):
    return ','.join(values) + '\n'
