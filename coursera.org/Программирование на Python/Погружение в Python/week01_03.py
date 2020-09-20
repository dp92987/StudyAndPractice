import sys 

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

d = b**2-4*a*c

if d > 0:
	x1 = int((-1*b+d**0.5)/(2*a))
	x2 = int((-1*b-d**0.5)/(2*a))
elif d < 0:
	x1 = x2 = None
else:
	x1 = x2 = int(-(b/(2*a)))

print(x1, x2, sep='\n')
