def somarmultiplosnumeros(lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma

def multiplicarmultiplosnumeros(lista):
    multiplicacao = 1
    for valor in lista:
        multiplicacao = multiplicacao * valor
    return multiplicacao

def ehinteiro(numero):
    return numero % 1 == 0

def ehpar(numero):
    if ehinteiro and numero % 2 == 0:
        return True
    else:
        return False

print(somarmultiplosnumeros([5, 10, 15]))
print(somarmultiplosnumeros([0.5, -4, 2]))

print(multiplicarmultiplosnumeros([2, 5]))
print(multiplicarmultiplosnumeros([-1, 3, 2.5]))

print(ehpar(8))
print(ehpar(5))
print(ehpar(2.5))
print(ehpar(2.0))

print(ehinteiro(10))
print(ehinteiro(-6))
print(ehinteiro(4.2))
