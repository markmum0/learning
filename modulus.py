# modulus operator %
while True:
	if 100 % 2 > 0:
		print('holy shit')# there is a reminder
	else:
		print('that was a close one')# no remainders
	break

x = 6 % 5
print(x)

#fmod is best applicable for the floating points 
import math
y = math.fmod(-6, 5)
print(y)

#divmod function performs both the division and the modular operations
z = divmod(6, 2)
print(z)

# the remainder theory doesnt allow for negative remainders so the remainder of -x % y should be postive
b = -6 % 5
print(b)