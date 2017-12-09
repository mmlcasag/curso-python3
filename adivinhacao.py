import random

def start() :
    print("===========================")
    print("=== Jogo de Adivinhação ===")
    print("===========================")

    # inicializa os pontos
    int_pontos = 1000

    # sorteia um número de 1 até 100
    int_numero = random.randrange(1,101)
    str_numero = str(int_numero)
    print(int_numero)

    # define o nível de dificuldade
    print("Dado os níveis de dificuldade:")
    print("(1) Facil")
    print("(2) Médio")
    print("(3) Difícil")
    str_nivel = input("Defina o nível de dificuldade: ")
    int_nivel = int(str_nivel)

    # define a quantidade de tentativas
    if   (int_nivel == 1):
        int_tentativas = 10
    elif (int_nivel == 2):
        int_tentativas = 6
    else:
        int_tentativas = 3

    for int_rodadas in range(1, int_tentativas + 1):
        print("")
        print("Tentativa", int_rodadas)

        str_palpite = input("Digite um número entre 1 e 100: ")
        int_palpite = int(str_palpite)

        print("O seu palpite foi:", str_palpite)

        if (int_palpite < 1 or int_palpite > 100):
            print("Você digitou um valor inválido. Perdeu a rodada!")
            continue

        bol_acertou = int_palpite == int_numero
        bol_maior = int_palpite > int_numero
        bol_menor = int_palpite < int_numero

        if (bol_acertou):
            print("Parabéns! Você acertou!")
            print("Total de pontos feitos {}".format(int_pontos))
            break
        elif (bol_maior):
            print("Não! Valor muito alto! Tente um valor maior!")
        elif (bol_menor):
            print("Não! Valor muito baixo! Tente um valor menor!")

        int_pontos_perdidos = abs(int_numero - int_palpite)
        int_pontos = int_pontos - int_pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    start()