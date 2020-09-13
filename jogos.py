import adivinhacao
import forca

def selecionar_jogo():
    print("Selecione o jogo que voce quer jogar: (1) Adivinhação, (2)Forca")
    jogo_selecionado = int(input("Defina sua Opção:"))

    if(jogo_selecionado == 1):
        adivinhacao.jogar()
    elif(jogo_selecionado == 2):
        forca.jogar()

if (__name__ == '__main__'):
    selecionar_jogo()