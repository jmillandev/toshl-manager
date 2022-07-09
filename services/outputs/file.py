from datetime import datetime

class FileOutput:

  def __init__(self, ext) -> None:
    self._ext = ext

  def out(self, body, title):
    date = datetime.now().strftime('%d-%m-%y-%H_%M_%S')
    title = f"{title}_{date}.toshl.{self._ext}"
    with open(title, 'w') as f:
      f.write(body)

    print(f"The file './{title}' was generated.")
