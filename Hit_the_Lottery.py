#Problem: https://codeforces.com/problemset/problem/996/A

amt = input() #capture input
amt=int(amt)

bills = [20,10,5,1] #$ bills, no need for $100 (see below)
count=0 #count for bills

if amt >= 100:
	a=divmod(amt,100) #get quotient and remainder
	amt=a[1]  #remainder
	count=a[0] #quotient

for b in bills: #for remaning money loop through bill types
	while b <= amt: #if divisible by bill
		amt=amt-b #subtract money
		count=count+1 #increment counter
		
print(count)
