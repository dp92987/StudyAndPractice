# coding=utf-8

"""
int() также в рамках перевода строки в число:

1. удаляет из начала и из концца строки пробелы, табы и т.д.:
' '     space
'\n'    newline
'\t'    horizontal tab
'\v'    vertical tab
'\f'    form feed
'\r'    Carraige return

2. принимает аргумент base - систему счисления:
    * по умолчанию 10
    * должен быть от 2 до 36 или 0
    * при base=0 функция выбирает систему по префиксу:
        0b/0B  base-2
        0o/0O  base-8
        0x/0X  base-16
    * если префикс не указан, то считает base=10
    
3. проверяет  на пустую строку

4. проверяет префикс - если есть и соотвествует системе, то учитывает его в далнейших вычислениях
"""

def str2int(s, base=10):
  # Проверяем, что s это string
  if not isinstance(s, str):
    raise TypeError(f"str2int() argument must be a string, not '{type(s)}'")

  # Проверяем, что base это integer
  if not isinstance(base, int):
    raise TypeError(f"str2int() argument must be an integer, not '{type(s)}'")

  # Проверяем, что base 0 или от 2 до 36
  if (base != 0 and base < 2) or base > 36:
    raise ValueError(f'str2int() base must be >= 2 and <= 36')

  # Убираем whitespaces и переводим в нижний регистр
  string = s.strip()
  string = string.lower()

  # Проверяем на пустую строку
  if string == '':
    raise ValueError(f"invalid literal for str2int() with base {base}: '{s}'")

  # Учитываем знак и удаляем его, если есть
  sign = 1
  if string[0] in '+-':
    if string[0] == '-':
      sign = -1
    string = string[1:]

  # Проверяем на допустимые символы (0-9 и a-z)
  for char in string:
    if not (ord(char) in range(48, 58) or ord(char) in range(97, 123)):
      raise ValueError(f"invalid literal for str2int() with base {base}: '{s}'")

  # Если система счисления 0, то по префиксу определяем подходящую
  # Если префикса нет, то считаем, что base=10
  base_dict = {'0b': 2, '0o': 8, '0x': 16}
  prefix = string[0:2].lower()
  if base == 0:
    if prefix == '0b' or prefix == '0o' or prefix == '0x':
      base = base_dict[prefix]
    else:
      base = 10

  # Удаляем префикс, если он есть и соотвествует системе
  if (base == 2 and prefix == '0b') \
      or (base == 8 and prefix == '0o') \
      or (base == 16 and prefix == '0x'):
    string = string[2:]

  # Считаем число
  total = 0
  for char in string:
    # Если от 0 до 9
    if ord(char) < 58:
      number = ord(char) - ord('0')
    # Если от a до z
    else:
      number = ord(char) - ord('a') + 10
    # Если число больше base
    if number >= base:
      raise ValueError(f"invalid literal for str2int() with base {base}: '{s}'")
    # Всё ок, складываем
    total = total*base + number

  # Возвращаем результат учитывая знак
  return sign * total


assert str2int(' -00420123') == int(' -00420123')
assert str2int(' -00420123         ') == int(' -00420123         ')
assert str2int('-0x10', base=0) == int('-0x10', base=0)
assert str2int('0b13', base=16) == int('0b13', base=16)
assert str2int('aa', base=36) == int('aa', base=36)
assert str2int('+aa', base=33) == int('+aa', base=33)
assert str2int('0b10', base=0) == int('0b10', base=0)
assert str2int('0b10', base=16) == int('0b10', base=16)

# print(str2int(' '))
# print(str2int('2%0'))
# print(str2int('10', base=None))
