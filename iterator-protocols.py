def first(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration:
    raise ValueError("iterable is empty")