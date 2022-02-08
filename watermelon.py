#https://codeforces.com/problemset/problem/4/A

w = input() #capture input
w = int(w)

if w>2:
	split = w-2
	if (split % 2) == 0:
		print("YES")
	else:
			print("NO")
else:
	print("NO")
