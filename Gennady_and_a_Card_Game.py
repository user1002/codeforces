#Problem:https://codeforces.com/problemset/problem/1097/A

me=input() #collect my hand
hand=[]
hand=list(me) #use list to break 'JH' to 'J''H'

cards=input() #collect table cards
table=[]
table=list(cards) #same as above
table= [i for i in table if i != ' '] #remove spaces

match='NO' #default variable to no

for h in hand:
	if h in table:
		match='YES'
		break #exit loop if true

print(match)