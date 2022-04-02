#https://codeforces.com/problemset/problem/1380/A

n = int(input())

for i in range(0, n):
	count = int(input())
	perm = input()
	perm = perm.split()
	a = [int(i) for i in perm]

	x = 0
	for i in range(0,len(a)-2):	
		if(a[i]<a[i+1]) and (a[i+1]>a[i+2]):
			x = x+1
			print('YES')
			print(a.index(a[i])+1,a.index(a[i+1])+1,a.index(a[i+2])+1)
			break
		else:
			continue
	if x==0:
		print('NO')
