#https://projecteuler.net/problem=1
#solution created by Tommy Tang https://github.com/jiaoziren

#make an empty list to store all numbers
stack = []

for i in range(1000):
	if i%3 == 0 or i%5 == 0:
		stack.append(i)

#sum of all numbers in the list
print stack
print sum(stack)