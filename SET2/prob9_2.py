a=dict(fak23ms153=12345,das23ms163=1363812,hdd23ms165=23527)
b=input("Enter User-ID")
if b in a :
   c=int(input("Enter Your Password"))
   if a[b]==c:
      print("Welcome to the Portal")
   else:
      print("Invalid Credentials")
else:
   print("Invalid Credentials")
   
if b in a:
   d=int(input("Enter New Password"))
   e=int(input("Enter New Password Again"))
   if d==e and d!=a[b] :
       a[b]=d
   else:
       print("Passwords Don't Match")
else:
   print("Invalid Username")
print(a)
