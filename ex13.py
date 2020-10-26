numero = int(input("Digite o numero -->"))
expoente = int(input("Digite o expoente -->"))
resultado = 0
for x in range(1,expoente):
    resultado = numero*numero

print(f'O resultado da potencia é {resultado}')