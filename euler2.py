result = 0
max = 20
for i in range(0,max):
  if i%2 == 0:
    result+=i

def fibonacci(n):


  if n==1 or n==2:
    return 1
  return fibonacci(n-1)+fibonacci(n-2)

print fibonacci(result)