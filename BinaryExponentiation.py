def power(a,b):
	res = 1 
	while b:
		if b%2 == 1:
			res *=a
		a *=a
		b /= b
	return res


print(power(2,10))