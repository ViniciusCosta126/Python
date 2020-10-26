while True:
    nota = int(input("Digite um numero de 0 a 10 -->"))

    if nota < 0 or nota > 10:
        print("Numeros invalidos")
    else:
        print("Voce digitou um valor valido")
        break