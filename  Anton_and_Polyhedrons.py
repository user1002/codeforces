#Problem: https://codeforces.com/problemset/problem/785/A

shp_dict={'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20} #create dict
shp_list=[] #initialize list
faces=0 #set variable to 0

n=int(input()) #collect user input

#create n number of inputs
while n != 0:
	a=input()
	shp_list.append(a)
	n = n-1

for s in shp_list: #loop through list
	faces = faces + shp_dict.get(s) #sum dictionary value

print(faces)