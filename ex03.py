nome = input("Digite seu nome -->")
idade = int(input("Digite sua idade -->"))
salario = float(input("Digite seu salario -->"))
sexo = input("Digite seu sexo (M/F) -->").upper()
estado = input("Digite seu estado civil -->").upper()w

while len(nome) < 3:
    nome = input("Digite seu nome -->")

while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade -->"))

while salario < 0:
    salario = float(input("Digite seu salario -->"))

while sexo != "M" or sexo != "F":
    sexo = input("Digite seu sexo (M/F) -->").upper()

while estado != "S" or estado != "C" or estado != "V" or estado != "D":
    estado = input("Digite seu estado civil (S/N/C/V/D) -->").upper()