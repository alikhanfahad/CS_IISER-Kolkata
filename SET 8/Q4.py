import numpy as np

marks1=[]
marks2=[]
marks3=[]
name=input("Enter Your Name")
sub1=int(input("Enter Marks of Subject 1"))
marks1.append(sub1)
sub2=int(input("Enter Marks of Subject 2"))
marks1.append(sub2)
sub3=int(input("Enter Marks of Subject 3"))
marks1.append(sub3)
   
name=input("Enter Your Name")
sub1=int(input("Enter Marks of Subject 1"))
marks2.append(sub1)
sub2=int(input("Enter Marks of Subject 2"))
marks2.append(sub2)
sub3=int(input("Enter Marks of Subject 3"))
marks2.append(sub3)

name=input("Enter Your Name")
sub1=int(input("Enter Marks of Subject 1"))
marks3.append(sub1)
sub2=int(input("Enter Marks of Subject 2"))
marks3.append(sub2)
sub3=int(input("Enter Marks of Subject 3"))
marks3.append(sub3)

marks1=np.array(marks1)
marks2=np.array(marks2)
marks3=np.array(marks3)
marks=np.stack((marks1,marks2,marks3))
avg=np.mean(marks,axis=0)
print(avg)
print(marks)

