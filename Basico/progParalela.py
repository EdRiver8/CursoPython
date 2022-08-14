import multiprocessing

numeros = [32,31,30,29,28]
"""
def cubo (n):
  return n ** 3

res = list(map(cubo, numeros))
print(res)

p = multiprocessing.Pool() 
print(p.map(cubo, numeros))
"""
def fib(n):    
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2) 

print(fib(numeros[0]))
print(fib(numeros[1]))
print(fib(numeros[2]))
print(fib(numeros[3]))
print(fib(numeros[4]))
"""
resF = list(map(fib, numeros))
print(resF)
"""
p = multiprocessing.Pool() 
print(p.map(fib,numeros))