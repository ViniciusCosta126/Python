a = int(input("Digite a populacao do pais A ->"))
taxa_a = float(input("Digite a taxa de crescimento do A ->"))
b = int(input("Digite a populacao do pais B ->"))
taxa_b = float(input("Digite a taxa de crescimento do B ->"))
anos = 0
while a < 0:
    a = int(input("Digite a populacao do pais A ->"))
while b < 0:
    b = int(input("Digite a populacao do pais B ->"))
while taxa_a < 0:
    taxa_a = float(input("Digite a taxa de crescimento do pais A"))
while taxa_b < 0:
    taxa_b = float(input("Digite a taxa de crescimento do pais B"))

taxa_a = taxa_a / 100
taxa_b = taxa_b / 100

if b > a:
    while  b > a:
        a = (a * taxa_a) + a
        b = (b * taxa_b) + b
        anos += 1
    print(f'Demorou {anos} anos para o Pais A passar o B')

else:
    while a > b:
        a = (a * taxa_a) + a
        b = (b * taxa_b) + b
        anos += 1
    print(f'Demorou {anos} anos para o Pais B passar o A')