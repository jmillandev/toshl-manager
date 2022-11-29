class ToshlError(Exception):
  
  def __init__(self, message) -> None:
    super().__init__(f"ERROR-TOSHL:: {message}")

class RequestToshlError(ToshlError):

  def __init__(self, method, url, extra_params, resp_data, status_reponse):
    msg = f"Request: -X {method} {url} --extra_params {extra_params} -> " \
              f"Response({status_reponse}): {resp_data}"
    super().__init__(msg)
