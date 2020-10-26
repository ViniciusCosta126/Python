while True:
    nome = input("Digite o nome de usuario -->").upper()
    senha = input("Digite a senha -->").upper()

    if nome == senha:
        print("Voce digitou nome e senha iguais, por favor faca novamente")
    else:
        print("Parabens, cadastrado com sucesso!!")
        break