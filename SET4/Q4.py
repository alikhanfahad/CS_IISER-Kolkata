s=input("Enter Name")
if len(s) % 2 == 0:
         y=len(s)//2
         s=s[y:]+s[0:y]
         print(s)
else:
         z=len(s)//2
         s=s[z+1:]+s[z]+s[0:z]
         print(s)


