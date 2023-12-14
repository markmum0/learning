num = list()
while True:
	inp = input("Enter a number: ")
	if inp == "ok" : break
	value = float(inp)
	num.append(value)
average = (sum(num)/len(num))
print(average)
