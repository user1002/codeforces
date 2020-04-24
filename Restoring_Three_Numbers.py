# Problem: https://codeforces.com/problemset/problem/1154/A

n = input() # collect user input

#split input and add int to list
num = [] 
num = n.split()
num = [int(i) for i in num] 
num.sort()

#assign each number to variable
a=num[0]
b=num[1]
c=num[2]
d=num[3]

# a b c d is given
# x y z is what we need to solve for
# solve for x
# x+y=a; x+z=b; x+y+z=d is what we know
# a-y = b-z = d-y-z equaling all x's

z = d-a
y = d-b
x = d-z-y

print(x,y,z)