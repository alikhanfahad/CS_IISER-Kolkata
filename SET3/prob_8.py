d = {1 : 'ONE', 2 : 'TWO', 3 : 'THREE', 4 : 'FOUR', 5 : 'FIVE', 6 : 'SIX', 7 : 'SEVEN', 8 : 'EIGHT', 9 : 'NINE'}
a=1234
b=str(a)
y=[]
for x in range(len(b)):
     z=int(b[x])
     y.append(d[z])
for w in range(len(y)):
    print(y[w],end=" ")
print(' ')
