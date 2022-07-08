def format_value(value):
  if isinstance(value, str):
    return value

  return f"{value:.2f}"


def format_values_to_str(dictionary):
  return { key: format_value(value) for key, value in dictionary.items() }
