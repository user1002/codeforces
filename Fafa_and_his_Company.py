# Problem: https://codeforces.com/problemset/problem/935/A

e=int(input()) # emp count

counter=0 #count of ways to distribute
n = e # total num of emp

while n>1:
	n=n-1 #employee count after taking out a leader
	l=e-n #leader count
	if n % l == 0: #if no remainder
		counter=counter+1

print(counter)		