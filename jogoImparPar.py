from random import randint
v = 0
vencedor = "JOGADOR"
criterio = ""                                 #declarando variáveis e importanto biblioteca
while vencedor == "JOGADOR":
    print("="*28)
    print("<<< JOGO DO PAR OU IMPAR >>>")
    print("="*28)
    computador = randint(0, 10)               #num do computador
    num = int(input("Informe um número: "))   #num do jogador
    criterio = str(input("Par ou Ímpar? [P/I] ")).upper() #criterio escolhido (ímpar ou par)

    if criterio == "P":
        print("PAR")

    elif criterio == "I":
        print("ÍMPAR")
    else:
        print("INVÁLIDO, tente novamente...")
        break
   
    operação = computador + num              
    print("")
    print(f"Você jogou {num} e o computadador {computador} = {num + computador}.")
    print("")

    if operação % 2 == 0:                    #se for PAR:
        if criterio == "P":
            print(f">>> O JOGADOR VENCEU! <<<")
            v += 1
        else:
            print(f">>> O COMPUTADOR VENCEU! <<<")
            vencedor = "COMPUTADOR"   

    else:                                    #se for ÍMPAR:
        if criterio == "I":
            print(f">>> O JOGADOR VENCEU! <<<")
            v += 1
        else:
            print(f">>> O COMPUTADOR VENCEU! <<<") 
            vencedor = "COMPUTADOR"
print("")
print(f"{v} vitórias seguidas para JOGADOR.")
print("GAME OVER...")
