#https://codeforces.com/problemset/problem/158/A

inpt = input()
inpt = inpt.split()

n = int(inpt[0])
k = int(inpt[1])
s = k-1

scores = input()
scores = scores.split()
scores = [int(i) for i in scores]

pass_score = scores[s]

filtered = []

for score in scores:
    if score >= pass_score and score > 0:
        filtered.append(score)

print(len(filtered))
