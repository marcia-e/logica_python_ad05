nomes_aprovados = ["João", "Maria", "Pedro", "Mariana"]

nome = input("Digite o seu nome: ").strip()
#strip olha se tem espaço depois do nome

#converte o nome digitado e o nome da lista para tudo minusculo e compara a lista
if nome.lower() in [n.lower() for n in nomes_aprovados]: #n guarda o nome digitado
    print (f"{nome} aprovado(a)!")
else:
    print (f"{nome} reprovado(a)!")
