#https://codeforces.com/problemset/problem/231/A

n = int(input())
final = []

for i in range(0, n):
	score = input()
	score = score.split()
	score = [int(i) for i in score]
	n_score = score[0]+score[1]+score[2]
	if n_score > 1:
		final.append(n_score)
	
print(len(final))
