import math

fib_number = int(input('Insira um número:'))

# 0, 1, 1, 2, 3, 5,

# Precisa ser um quadrado perfeito
# (5*n^2 + 4) ou (5*n^2 - 4)
def teste_quadrado(number):
    x = int(math.sqrt(number))
    if x * x == number:
        return True
    else:
        return False
    

def teste_fib(number):
    fnc = 5 * math.pow(number,2)
    return teste_quadrado(fnc + 4) or teste_quadrado(fnc - 4)

if teste_fib(fib_number):
    print(f'É da sequencia de fibonacci.')
if not teste_fib(fib_number):
    print('Não pertence a sequência de fibonacci.')

