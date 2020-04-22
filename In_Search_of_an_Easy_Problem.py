# Problem: https://codeforces.com/problemset/problem/1030/A

n=int(input()) #capture sample size
score=input() #capture feedack

#compute output
feedback=[]
feedback = score.split()
mytuple=tuple(feedback)

if '1' in mytuple:
    print('HARD')
else:
    print('EASY')