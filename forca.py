import random


def imprime_mensagem_abertura():
    print("=====================")
    print("=== Jogo da Forca ===")
    print("=====================")


def carrega_palavra_secreta():
    lista_palavras = []

    arquivo_texto = open("arquivo.txt", "r")
    for linha in arquivo_texto:
        lista_palavras.append(linha.strip())
    arquivo_texto.close()

    posicao_aleatoria = random.randrange(0, len(lista_palavras))

    return lista_palavras[posicao_aleatoria].upper()


def inicializa_letras_forca(str_palavra):
    return ["_" for str_letra in str_palavra]


def solicita_palpite_usuario():
    str_palpite = input("Qual letra? ")
    return str_palpite.upper().strip()


def marca_palpite_correto(str_palpite, str_palavra, arr_letras_forca):
    int_posicao = 0
    for str_letra in str_palavra:
        int_posicao = int_posicao + 1
        if (str_palpite == str_letra):
            arr_letras_forca[int_posicao - 1] = str_palpite
    print(arr_letras_forca)


def marca_palpite_incorreto(int_erros):
    int_erros = int_erros + 1
    print("  _______     ")
    print(" |/      |    ")

    if(int_erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(int_erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(int_erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(int_erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(int_erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(int_erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(int_erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    return int_erros


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(str_palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(str_palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def start():
    imprime_mensagem_abertura()
    str_palavra = carrega_palavra_secreta()
    arr_letras_forca = inicializa_letras_forca(str_palavra)

    int_erros = 0
    bol_virou = False
    bol_morreu = False

    while (not bol_virou and not bol_morreu):
        str_palpite = solicita_palpite_usuario()

        if (str_palpite in str_palavra):
            marca_palpite_correto(str_palpite, str_palavra, arr_letras_forca)
        else:
            int_erros = marca_palpite_incorreto(int_erros)

        bol_virou = arr_letras_forca.count("_") == 0
        bol_morreu = int_erros >= 7

    if (bol_virou):
        imprime_mensagem_vencedor()
    if (bol_morreu):
        imprime_mensagem_perdedor(str_palavra)

if (__name__ == "__main__"):
    start()