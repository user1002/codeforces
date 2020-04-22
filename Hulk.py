#Problem: https://codeforces.com/problemset/problem/705/A

input_counter=int(input())
counter=0
start='I hate'
space=' '
feel=''
evenfeel='that I love'
oddfeel='that I hate'
end = 'it'

if input_counter == 1: #set by default to 'I hate it' by rule
	pass
else:
	while input_counter != counter+1: #counter+1, since I am start execution at 0
		if (counter % 2)==0:
			feel=feel+space+evenfeel
		else:
			feel=feel+space+oddfeel
		counter += 1

print(start+feel+space+end)