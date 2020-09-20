import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data()  # вернёт '{"data": 42}'
