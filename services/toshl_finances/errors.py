class ToshlError(Exception):
  
  def __init__(self, message) -> None:
    super().__init__(f"ERROR-TOSHL:: {message}")

class RequestToshlError(ToshlError):

  def __init__(self, method, url, data, resp_data, status_reponse):
    msg = f"Request: -X {method} {url} --data {data} -> " \
              f"Response({status_reponse}): {resp_data}"
    super().__init__(msg)
