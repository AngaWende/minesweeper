from random import randint
numero_de_casas = 10
numero_de_bombas = 15

tabuleiro = []

def criar_tabuleiro():
    global tabuleiro
    tabuleiro = [[0 for l in range(numero_de_casas)] for c in range(numero_de_casas)]

criar_tabuleiro()
tab_visivel = [[" " for l in range(numero_de_casas)] for c in range(numero_de_casas)]

posicoes_das_bombas = []
def colocar_bombas():
    bombas_colocadas = 0

    while bombas_colocadas < numero_de_bombas:
        linha = randint(0, numero_de_casas-1)
        coluna = randint(0, numero_de_casas-1)

        if tabuleiro[linha][coluna] == '*':
            continue
        else:
            tabuleiro[linha][coluna] = '*'
        posicoes_das_bombas.append(f'{linha}{coluna}')
        bombas_colocadas+=1


colocar_bombas()

def colocar_numeros_de_bombas_ao_redor():
    for x in posicoes_das_bombas:
        lin = int(x[0])
        col = int(x[1])
        if lin > 0 and col > 0 and tabuleiro[lin - 1][col - 1] != '*':
            tabuleiro[lin - 1][col - 1] += 1

        if lin > 0 and tabuleiro[lin - 1][col] != '*':
            tabuleiro[lin - 1][col] += 1

        if lin > 0 and col < numero_de_casas - 1 and tabuleiro[lin - 1][col + 1] != '*':
            tabuleiro[lin - 1][col + 1] += 1

        if col > 0 and tabuleiro[lin][col - 1] != '*':
            tabuleiro[lin][col - 1] += 1

        if col < numero_de_casas - 1 and tabuleiro[lin][col + 1] != '*':
            tabuleiro[lin][col + 1] += 1

        if lin < numero_de_casas - 1 and col > 0 and tabuleiro[lin + 1][col - 1] != '*':
            tabuleiro[lin + 1][col - 1] += 1

        if lin < numero_de_casas - 1 and tabuleiro[lin + 1][col] != '*':
            tabuleiro[lin + 1][col] += 1

        if lin < numero_de_casas - 1 and col < numero_de_casas - 1 and tabuleiro[lin + 1][col + 1] != '*':
            tabuleiro[lin + 1][col + 1] += 1


def campos_adjacentes(linha, coluna):
    lin = linha
    col = coluna
    campos = []

    if lin - 1 >= 0 and col - 1 >= 0:
        campos.append([lin - 1, col - 1])

    if lin - 1 >= 0 and col == col:
        campos.append([lin - 1, col])

    if lin - 1 >= 0 and col + 1 < numero_de_casas:
        campos.append([lin - 1, col + 1])

    if col - 1 >= 0 and lin == lin:
        campos.append([lin, col - 1])

    if col + 1 < numero_de_casas:
        campos.append([lin, col + 1])

    if lin + 1 < numero_de_casas and col - 1 >= 0:
        campos.append([lin + 1, col - 1])

    if lin + 1 < numero_de_casas and col == col:
        campos.append([lin + 1, col])

    if lin + 1 < numero_de_casas and col + 1 < numero_de_casas:
        campos.append([lin + 1, col + 1])

    return campos


def mostrar_campos(linha, coluna):
    #CRIAR UMA LISTA COM O CAMPO A VERIFICAR AS CASAS LATERAIS
    campos = campos_adjacentes(linha, coluna)

    campos_com_0 = []

    #SE O VALOR FOR MAIOR QUE ZERO MOSTRAR O VALOR (COPIAR DO TABULEIRO ORIGINAL PRO RESERVA)

    for i in campos:
        # if tabuleiro[i[0]][i[1]] == 0:
        #     mostrar_campos(i[0], i[1])
        if tabuleiro[i[0]][i[1]] != '*' and tabuleiro[i[0]][i[1]] >= 0:
            tab_visivel[i[0]][i[1]] = tabuleiro[i[0]][i[1]]

def mostrar_campos_2():

    continuar = 0

    while continuar < numero_de_casas **2:
        cont = 0
        continuar += 1
        for l in tab_visivel:
            cont2 = 0
            for c in l:
                if c == 0:
                    mostrar_campos(cont,cont2)

                cont2+=1
            cont+=1




def casas_vagas():
    contador = 0
    for l in tab_visivel:
        for c in l:
            if c == ' ':
                contador+=1

    return contador


colocar_numeros_de_bombas_ao_redor()


def show_tab(tab):
    tab = tab
    cont = 0
    print('      ', end='')
    for i in range(numero_de_casas):
        print(f'{i}   ', end='')
    print()
    print('____', end='')
    for i in range(numero_de_casas):
        print(f'____', end='')
    print()
    for l in tab:

        print(cont, end='   |')
        for c in l:
            print(f' {c} |', end='')
        cont+=1
        print()
        # print()

show_tab(tabuleiro)
show_tab(tab_visivel)
# print(tab_reserva)

def jogar():
    while True:
        coordenadas = input(f'Digite as coordenadas de 0 a {numero_de_casas - 1} (linha e coluna): ')
        linha = int(coordenadas[0])
        coluna = int(coordenadas[1])

        if tabuleiro[linha][coluna] != '*':
            tab_visivel[linha][coluna] = tabuleiro[linha][coluna]
            if tabuleiro[linha][coluna] == 0:
                mostrar_campos(linha, coluna)
                mostrar_campos_2()
            show_tab(tab_visivel)
        else:
            print('VOCÊ EXPLODIU UMA BOMBA!!!')
            show_tab(tabuleiro)
            break

        if casas_vagas() == numero_de_bombas:
            print('PARABÉNS, VOCÊ GANHOU!!!!!')

jogar()