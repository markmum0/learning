d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
#print(t)
for k, v in t:
	print(k, v)

temp = list()
for k,v in d.items():
	newtup = (v, k)
	temp.append(newtup)
#print(temp)
temp = sorted(temp, reverse=True)# the reverse=True changes from highest to lowest
print(temp)