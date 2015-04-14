'''I stole the algorithm and code from this answer on SO - it's just too good that I'm not even ashamed to copy.'''
'''http://stackoverflow.com/a/412942/112328'''

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors

pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs)
print largest_prime_factor
print pfs
