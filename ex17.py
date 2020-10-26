numero = int(input("Digite o numero desejado -->"))
resultado = 1
for c in range(numero, 0, -1):
    resultado = resultado * c

print(f'O resultado do fatorial é {resultado}')