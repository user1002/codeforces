#https://codeforces.com/problemset/problem/282/A

n = int(input())
operation = []

x = 0

for i in range(0, n):
	op = input()
	op = op.replace('X','')
	if op == '++':
		x = x + 1
	else:
		x = x - 1
			
print(x)
