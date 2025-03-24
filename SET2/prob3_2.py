a=input("Enter Your Name")
b=a.split()
c=b[0][0]+'.'
for x in range(1,len(b)-1,1):
    c+=b[x][0]+'.'
c+=b[len(b)-1]
print(c)
