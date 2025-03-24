d={"Where is IISER-Kolkata":[('kolkata',0,0),('kalyani',1,2)],"Where is CESSI?":[('kolkata',0,0),('kalyani',1,4)]}
a=d.keys()
a=list(a)
b=d.values()
b=list(b)
score=0
for x in range(len(a)):
    print(a[x])
    print("\n")
    print("Option 1 ",b[x][0][0])
    print("Option 2",b[x][1][0])
    ans=input("Enter Answer")
    if ans==b[x][1][0]:
       score+=b[x][1][2]
       print("Correct Answer")
    else:
       print("Wrong Answer")
print(score)
if score<3:
   print("Congrats you won 1 lakh rupees")
else:
   print("Jackpot Question: Where is Chem Lab?")
   jackpot_answer="aac"
   input_answer=input("Enter Answer")
   if jackpot_answer==input_answer:
      print("You have won 10 crore")
   else:
      print("Congrats you won 1 lakh rupees")

  


