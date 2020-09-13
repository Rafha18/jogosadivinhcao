import random


def jogar():
    print("Bem-Vindo ao Jogo")

    # numero_objetivo = 99
    numero_objetivo = round(random.randrange(1, 101))
    # print(f"O Sorteado foi: {numero_objetivo}")
    numero_tentativas = 5
    tentativa = 1

    numero_pontos = 1000
    print("Selecione o nivel de dificuldade:")
    print("(1) Fácil, (2) Médio, (3) Dificil")

    dificuldade = int(input("Selecione a dificuldade: "))

    if(dificuldade < 1 or dificuldade > 3):
        print("Dificuldade Invalida")
        jogar()

    if(dificuldade == 1):
        numero_tentativas = 15
    elif(dificuldade == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    while (tentativa <= numero_tentativas):
        print(f"Voce esta na tentativa {tentativa}, de um total de {numero_tentativas}.")

        chute_string = input("Qual o seu chute? (1-100)")
        chute = int(chute_string)

        if (chute < 1 or chute > 100):
            print("Voce Digitou um Numero Invalido!")
            exit()

        acertou = (chute == numero_objetivo)
        maior = chute > numero_objetivo
        menor = chute < numero_objetivo

        print(f"Voce Chutou: {chute_string}")

        if (acertou):
            print(f"Voce acertou Parabéns! Você fez um total de {numero_pontos} Pontos.")
            break
        else:
            if (maior):
                print("Você ERROU, o numero é MAIOR!")
            elif (menor):
                print("Você Errou, este numero é MENOR")
            pontos_perdidos = 10
            numero_pontos -= pontos_perdidos
            print(f"Voce tem um total de {numero_pontos} Pontos!")

        tentativa += 1

    print(f"fim de jogo, o numero correto era {numero_objetivo}, Voce perdeu todos os seus Pontos!")


if (__name__ == '__main__'):
    jogar()
