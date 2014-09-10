#@tiggreen
# Greatest Common Divisor (GCD). Euclidean algorithm.
def gcd(m,n):
	if m % n == 0:
		return n
	else:
		return gcd(n, m%n)

def main():
	m = int(input("m: "))
	n = int(input("n: "))
	print(gcd(m,n))

main()