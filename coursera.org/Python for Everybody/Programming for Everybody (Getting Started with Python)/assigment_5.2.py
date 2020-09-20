largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
      break
    try:
      num_int = int(num)
    except:
      print('Invalid input')
      continue
    if smallest is None and largest is None:
      smallest = num_int
      largest = num_int
    else:
      if num_int < smallest:
        smallest = num_int
      if num_int > largest:
        largest = num_int

print("Maximum is", largest)
print("Minimum is", smallest)
