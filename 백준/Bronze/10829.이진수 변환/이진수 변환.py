import sys
input = sys.stdin.readline

def DtoB(n):
	if n <= 1:
		return str(n)
	return DtoB(n // 2) + DtoB(n % 2)


print(DtoB(int(input())))