multiple = 3
multiple2 = 5
result = 0
max = 1000
for i in range(0,max):
	if i%multiple == 0 or i%multiple2 == 0:
		result += i

print result
