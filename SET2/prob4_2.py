fibonacci_list=[1,1]
def fibonacci(n):
     for x in range(1,n+1,1):
         c=fibonacci_list[x]+fibonacci_list[x-1]
         fibonacci_list.append(c)
     return fibonacci_list
n=10
fibonacci(n)
print(fibonacci_list)
for z in range(n):
    print(fibonacci_list[z],'')
fibonacci_string=''.join(str(xs) for xs in fibonacci_list)

    
