# Função sem retorno e sem parâmetros
def sobre():
    print ("Desenvolvido por: Marcia de Paiva")

# Função sem retorno e com parâmetros | Obrigatório informar os parametros (se tiver)
def turma(turma):
    print (f"Turma: {turma}")

# Função com retorno e com parâmetros
def somar (numero1, numero2):
    return numero1 + numero2

sobre()
turma ("AD-O5")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = somar(numero1, numero2)
print (f"A soma de {numero1} + {numero2} = {resultado}")