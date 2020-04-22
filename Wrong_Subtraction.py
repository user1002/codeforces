# Problem: https://codeforces.com/problemset/problem/977/A

#Create function
def Tanya(n,k):
    while k > 0 and n > 1:
        if n <= 1:
            pass
        elif (n % 10) != 0:
            n=int(n-1)
        else:
            n=int(n/10)
        k=k-1
    print(n)

a=input() #collect input
n=int(a.split(' ')[0])
k=int(a.split(' ')[1])

#pass value to function
Tanya(n,k)