a=[]
n=int(input("Enter a number:"))
for x in range(n):
    b=input("Enter the name")
    a.append(b)
    c=input("Enter the age")
    a.append(c)
print(a)

d={}

for y in range(0,len(a),2):
    d[a[y]]=a[y+1]
print(d)
