import random


def jogar():
    print('*'*30)
    print('***Bem vindo ao jogo de forca***')
    print('*'*30)
    palavra_secreta = ""
    arquivo = open(
        "C:\\Users\\vimim\\Desktop\\python\\JOGO DA FORC\\palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha.strip()
        palavras.append(linha)
    arquivo.close()

    arquivo = open(
        "C:\\Users\\vimim\\Desktop\\python\\JOGO DA FORC\\dicas.txt", "r")
    dica = []
    for linha in arquivo:
        dica.append(linha)
    arquivo.close

    numero = random.randint(1, len(palavras))
    palavra_secreta = palavras[numero]
    letras_acertadas = []
    for c in range(1, len(palavra_secreta)):
        letras_acertadas.append("_")

    erros = 0
    enforcou = False
    acertou = False
    print(letras_acertadas)

    print(f'A dica da palavra é {dica[numero]}')
    while not enforcou and not acertou:
        chute = input("Digite uma letra -->").upper().strip()
        index = 0
        if(chute.upper() in palavra_secreta.upper()):
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            print("+="*40)
            print(f'Voce errou, tem apenas mais {6 - erros} chanches')
            print("+="*40)
        print(letras_acertadas)
        if "_" not in letras_acertadas:
            acertou = True
            print("*"*40)
            print('Parabens voce acertou a palavra')
            print(f'A palavra secreta era {palavra_secreta}')
            print("*"*40)
        if erros == 6:
            enforcou = True
            print("*"*40)
            print('Infelizmente voce perdeu')
            print(f'A palavra era {palavra_secreta}')
            print("*"*40)


if(__name__ == "__main__"):
    jogar()
