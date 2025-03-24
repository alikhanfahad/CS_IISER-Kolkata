a=[1,2,3,4,5,6,7,8,9]
y=[]
for x in range(len(a)-1):
    if a[x]<a[x+1]:
       y.append(1)
    else:
       print("Decreasing sequence")

if sum(y)==len(a)-1:
    print("Monotonic sequence")
else:
    print("Non Monotonic sequence")
       
       
