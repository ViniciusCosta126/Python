while True:
    numero = int(input("Digite o numero desejado -->"))
    if numero <= 16 and numero > 0:
        resultado = 1
        for c in range(numero, 0, -1):
            resultado = resultado * c
        print(f'O resultado do fatorial é {resultado}')
    else:
        print("Numero invalido")
        
    opcao = input("Deseja digitar um novo numero?? (S/N) ->").upper()
    if opcao == "N":
        break

        
