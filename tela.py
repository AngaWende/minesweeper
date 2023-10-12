''' TESTE DE TELA PARA CAMPO MINADO '''

import pygame as pg
from random import randint
from time import sleep
from main import *
from testes import *

pg.init()
PADRAO = 10
LINHAS, COLUNAS = PADRAO, PADRAO
CINZA_CLARO = (120,120,120)
CINZA_ESCURO = (70, 70, 70)
BRANCO = (255,255,255)
PRETO = (0,0,0)
AMARELO = (255,255,0)
VERMELHO = (255,0,0)

cor_da_casa = CINZA_CLARO


largura_do_quadrado = 35
numero_de_bombas = 15

fonte = pg.font.SysFont('arial', largura_do_quadrado // 1, True)

tela = pg.display.set_mode((LINHAS * largura_do_quadrado, COLUNAS * largura_do_quadrado))
tela.fill(CINZA_ESCURO)

# pg.draw.rect(tela, (255,255,0), (0,0,largura_do_quadrado,largura_do_quadrado), 1)
# pg.draw.polygon(tela, (AMARELO), (10,10,10,10))
casas = []
descricao_casas = []

def criar_quadrados():
    cont = 0
    for i in range(LINHAS):
        for j in range(COLUNAS):
            # posicao =

            casas.append((largura_do_quadrado * j, largura_do_quadrado * i))
            descricao_casas.append(f'linha: {i}, coluna: {j}, posição: {(largura_do_quadrado * i, largura_do_quadrado * j)}')
            pg.draw.rect(tela, PRETO, (largura_do_quadrado * i, largura_do_quadrado * j,largura_do_quadrado, largura_do_quadrado), 1)

criar_quadrados()
dict_casas = {}

#DICIONARIO DE CASAS
#CHAVE = NUMERO DA CASA
#VALORES = [ POSICAO   |   VALOR (NUMERO DE BOMBAS OU BOMBA)  |   STATUS (SE JÁ FOI REVELADA OU ESTÁ COM INTERROGAÇÃO   ]

for i in casas:
    # print(i)
    valor = '' if dict_casas_ocultas[casas.index(i)] == 0 else dict_casas_ocultas[casas.index(i)]
    dict_casas[casas.index(i)] = [i, valor, 0]

# for i, j in dict_casas.items():
#     print(i, j)

posicoes_das_bombas = []

def explosao():
    global cor_da_casa
    for i in range(len(dict_casas)):
        casas_visiveis.add(i)
        cor_da_casa = (255,99,71)


def selecionar_casa(pos, revelar):
    valor = [0,0]
    valor[0] = pos[0]
    valor[1] = pos[1]


    for i, j in dict_casas.items():


        # print(i, j)
        if valor[0] < j[0][0]+largura_do_quadrado and valor[1] < j[0][1]+largura_do_quadrado:
            print(j[2])

            if not revelar and i not in casas_visiveis:
                print('não revelada')
                txt = fonte.render('?', True, VERMELHO)
                tela.blit(txt, (j[0]))
            return i

def revelar_casas():


    for i, j in dict_casas.items():
        # print(i, type(i))
        if i in casas_visiveis:
            j[2] = 1
            pg.draw.rect(tela, cor_da_casa, (j[0][0], j[0][1], largura_do_quadrado, largura_do_quadrado))
            pg.draw.rect(tela, PRETO, (j[0][0], j[0][1], largura_do_quadrado, largura_do_quadrado), 1)
            txt = fonte.render(str(j[1]), True, PRETO)
            tela.blit(txt, (j[0]))

            # txt = fonte.render(str(j[1]), True, PRETO)

    # print('casas',casas_visiveis)


# # colocar_bombas()
# play()
while True:
    # sleep(5)
    pg.display.update()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()

        if e.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if e.button == 1:

                fim = anexar_tabelas(selecionar_casa(pos, True))

                if fim == 1:
                    explosao()
                elif fim == 0:
                    print('PARABÉNS')

                revelar_casas()
                print(pos)

            if e.button == 3:
                selecionar_casa(pos, False)




