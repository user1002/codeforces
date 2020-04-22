#Problem https://codeforces.com/problemset/problem/791/A

w=input()#collect input

wgt=[] #initialize list
wgt=w.split() #split input values
l=int(wgt[0])
b=int(wgt[1])
y=0

while l <= b:
	y=y+1
	l=l*3
	b=b*2

print(y)