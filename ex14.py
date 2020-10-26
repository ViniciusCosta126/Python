par = 0
impar = 0
for c in range(1,11):
    numero = int(input("Digite um numero -->"))
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1

print(f'Voce digitou {par} numeros pares e {impar} numeros impares')
