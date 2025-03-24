#Question 11
h=int(input("Enter Height of the Ball"))
n=int(input("Number of Steps"))
hnew=h
i=1
while hnew>0.05 and i<n+1:
     hnew=hnew/2
     i=i+1
     print(hnew)

