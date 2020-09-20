import sys

digit_string = sys.argv[1]

total = 0
for ch in digit_string:
	total += int(ch)

print(total)
