numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite um operador (+, -, * ou /): ")

resultado = ""

if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado da operação é: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado da operação é: {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado da operação é: {resultado}")
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da operação é: {resultado}")
    else:
        print("Não é possível dividir por 0")

else: 
    print("Operador inválido")


