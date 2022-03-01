#https://codeforces.com/problemset/problem/71/A

n = int(input())
word_list = []

for i in range(0, n):
    word = input()
    word_list.append(word)

for i in word_list:
	word_count = len(i)
	if word_count > 10:
		word_count_2 = len(i)-2
		print(i[0]+str(word_count_2)+i[-1:])
	else:
		print(i)
