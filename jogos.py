import adivinhacao
import forca

def menu():
    print("==========================")
    print("=== Escolha o seu jogo ===")
    print("==========================")

    # seleciona o jogo
    print("Dado os seguintes jogos:")
    print("(1) Jogo de Adivinhação")
    print("(2) Jogo da Forca")

    str_jogo = input("Qual jogo deseja jogar? ")
    int_jogo = int(str_jogo)

    if (int_jogo == 1) :
        adivinhacao.start()
    if (int_jogo == 2) :
        forca.start()

if (__name__ == "__main__"):
    menu()