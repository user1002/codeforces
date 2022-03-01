#https://codeforces.com/problemset/problem/50/A

nm = input()
nm = nm.split()
m = int(nm[0])
n = int(nm[1])
board = m*n
domino = 2
fit = int(board/domino)

print(fit)
