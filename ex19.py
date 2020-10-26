maior = 0
menor = 100000000000000000000
soma = 0

while True:
    numero = float(input("Digite um numero -->"))
    if numero < 0 or numero > 1000:
        while numero < 0 or numero >= 1000:
            numero = float(input("Digite um numero -->"))
    soma += numero
    if numero > maior:
        maior = numero
    if menor > numero:
        menor = numero
    opcao = input("Deseja continuar? (S/N) -->").upper()
    if opcao == "N":
        break
print(f'Maior numero = {maior} menor numero {menor} soma deles {soma}')