n1 = int(input("Digite o primeiro numero -->"))
n2 = int(input("Digite o segundo numero -->"))
soma = 0
if n1 > n2:
    for numeros in range(n2,n1+1):
        print(numeros)
        soma = soma + numeros
else:
    for numeros in range(n1,n2+1):
        print(numeros)
        soma = soma + numeros

print(f'A soma dos numeros é {soma}')