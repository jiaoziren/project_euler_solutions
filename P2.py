#https://projecteuler.net/problem=2
#solution created by Tommy Tang https://github.com/jiaoziren
list = []

a, b = 1, 2
while a < 4000000:
	list.append(a)
	a, b = b, a+b

print  sum(filter(lambda a: a%2 == 0, list))