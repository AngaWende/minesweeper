from random import randint
dim = 15
# qtde_linhas = 5
# qtde_colunas = 5
# numero_de_bombas = 2
qtde_linhas = 15
qtde_colunas = 15
numero_de_bombas = 100
posicoes_das_bombas = []


tab = [[0 for _ in range(qtde_colunas)] for _ in range(qtde_linhas)]

def colocar_bombas():
    bombas_colocadas = 0

    while bombas_colocadas < numero_de_bombas:
        linha = randint(0, qtde_linhas-1)
        coluna = randint(0, qtde_colunas-1)

        if tab[linha][coluna] == '*':
            continue
        else:
            tab[linha][coluna] = '*'
        posicoes_das_bombas.append([linha, coluna])
        bombas_colocadas+=1




def colocar_numeros_de_bombas_ao_redor():
    posicoes_proximas = []

    for i in posicoes_das_bombas:
        casas_proximas = casas_ao_redor(i)
        posicoes_proximas.extend(casas_proximas)

        for j in dic.values():
            if j[0] in casas_proximas:
                if j[1] != '*':
                    j[1] += 1



def casas_ao_redor(coordenada):
    linha = coordenada[0]
    coluna = coordenada[1]

    casas = []

    if linha - 1 >= 0 and coluna - 1 >= 0:
        casas.append([linha - 1, coluna -1])
    if linha- 1 >= 0:
        casas.append([linha - 1, coluna])
    if linha - 1 >=0 and coluna + 1 < qtde_colunas:
        casas.append([linha - 1, coluna +1])

    if coluna -1 >=0:
        casas.append([linha , coluna -1])
    if coluna +1 < qtde_colunas:
        casas.append([linha , coluna +1])

    if linha + 1 < qtde_linhas:
        casas.append([linha + 1, coluna])
        if coluna-1 >=0:
            casas.append([linha + 1, coluna - 1])
        if coluna +1 < qtde_colunas:
            casas.append([linha + 1, coluna + 1])

    return casas





dic = dict()


#DICIONÁRIO: 0 - COORDENADA LÓGICA DO TABULEIRO, [Nº DE LINHA, Nº DE COLUNA]
#            1 - VALOR CONTIDO NA CASA (BOMBA OU NÚMERO DE BOMBAS PRÓXIMAS)
#            2 - STATUS DA CASA (OCULTO - CASA NÃO REVELADA
#                                INTERROGAÇÃO - CASA MARCADA COMO DÚVIDA E BLOQUEADA PARA REVELAR
#                                REVELADA - CASA REVELADA AO CLICAR COM BOTÃO ESQUERDO
#                                ABERTA - CASA REVELADA POR CONTER 0 BOMBA AO REDOR)
#            3 - COORDENADA FÍSICA QUE TEM A POSIÇÃO DO CLIQUE NA TELA, [EIXO X, EIXO Y]
def criar_dicionario():
    global dic
    c_linha, c_col, c_geral = 0, 0, 0
    for i in tab:
        c_col = 0
        for j in i:
            dic[f'{c_linha},{c_col}'] = [[c_linha, c_col], j, 'oculto', []]
            # dic[c_geral] = [[c_linha, c_col], j, 0, []]
            c_col +=1
            c_geral+=1
        c_linha+=1





def mostrar_valor_por_coordenada(lin, col):
    for i in dic.values():
        if i[0] == [lin, col]:
            # print(i[1])
            return i[1]


def jogar():
    colocar_bombas()
    criar_dicionario()
    colocar_numeros_de_bombas_ao_redor()









