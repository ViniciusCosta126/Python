maior = 0
for c in range(0,5):
    numero = int(input("Digite um numero ->"))
    if numero > maior:
        maior = numero

print(f'O maior numero {maior}')