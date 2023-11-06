''' TESTE DE TELA PARA CAMPO MINADO '''

import pygame as pg
# from regras import *
from regras import *
pg.init()
# DIMENSOES = numero_de_casas
LINHAS, COLUNAS = qtde_linhas, qtde_colunas

CINZA_CLARO = (120, 120, 120)
CINZA_ESCURO = (70, 70, 70)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 99, 71)
VERMELHO_ESCURO = (255, 0, 0)
VERDE_CLARO = (152,251,152)
VERDE_BOMBA = (0,128,0)
cor_da_casa = CINZA_CLARO

largura_do_quadrado = 35

fonte = pg.font.SysFont('arial', largura_do_quadrado // 1, True)

tela = pg.display.set_mode((COLUNAS * largura_do_quadrado, LINHAS * largura_do_quadrado))
tela.fill(CINZA_ESCURO)

casas = []
primeira_jogada = True
contador_de_casas = 0

jogar()
def criar_quadrados():  #CRIA OS QUADRADOS E ADICIONA AS COORDENADAS NO DICIONARIO
    c = 0
    for i in range(LINHAS):
        for j in range(COLUNAS):

            dic[f'{i},{j}'][3] = (largura_do_quadrado * j, largura_do_quadrado * i)
            # print(largura_do_quadrado * j, largura_do_quadrado * i)
            casas.append((largura_do_quadrado * j, largura_do_quadrado * i))

            pg.draw.rect(tela, PRETO,
                         (largura_do_quadrado * j, largura_do_quadrado * i, largura_do_quadrado, largura_do_quadrado),
                         2)
            c+=1

criar_quadrados()
dict_casas = {}


def explosao():


    for j in dic.values():

        if j[1] == '*':

            pg.draw.rect(tela, VERMELHO_ESCURO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
            pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
            mina = pg.image.load('mina.png')
            tela.blit(mina, (j[3][0]+1, j[3][1]+1))
        else:

            pg.draw.rect(tela, VERMELHO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
            pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
            valor_do_campo = ' ' if str(j[1]) == '0' else str(j[1])
            txt = fonte.render(valor_do_campo, True, PRETO)
            tela.blit(txt, (j[3][0] + 6, j[3][1]))

def validar_vitoria():
    cont = 0
    for i in dic.values():
        if i[2] == 'revelado':
            cont += 1

    if cont == (LINHAS*COLUNAS) - numero_de_bombas:
        vitoria()

def vitoria():
    global cor_da_casa


    for j in dic.values():

        if j[1] == '*':
            pg.draw.rect(tela, VERDE_BOMBA, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
            pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
            flag = pg.image.load('flag.png')
            tela.blit(flag, (j[3][0] + 1, j[3][1] + 1))
        else:
            pg.draw.rect(tela, VERDE_CLARO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
            pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
            valor_do_campo = ' ' if j[1] == 0 else str(j[1])
            txt = fonte.render(valor_do_campo, True, PRETO)
            tela.blit(txt, (j[3][0] + 6, j[3][1]))

def selecionar_casa(pos, revelar):
    #REVELAR: 0 - CLIQUE COM O DIREITO
    #         1 - CLIQUE COM O ESQUERDO
    #         2 - ACIONADO PELO MÉTODO revelar_casas_vazias()

    valor = [0, 0]
    valor[0] = pos[0]
    valor[1] = pos[1]
    global contador_de_casas

    for j in dic.values():

        # print(i, j)
        if valor[0] < j[3][0] + largura_do_quadrado and valor[1] < j[3][1] + largura_do_quadrado:
            # print(j[2])
            if revelar != 0:
                if j[2] == 'oculto':
                    # if 'revelado' != j[2] != 'interrogação':
                    if j[1] == 0:
                        j[2] = 'revelado'
                        revelar_casas_vazias()
                        contador_de_casas += 1
                    if j[1] == '*':
                        global primeira_jogada
                        if primeira_jogada:
                            validar_primeira_jogada()
                        else:
                            explosao()
                            break


                    else:
                        pg.draw.rect(tela, CINZA_CLARO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
                        pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
                        valor_do_campo = ' ' if j[1] == 0 else str(j[1])
                        txt = fonte.render(valor_do_campo, True, PRETO)
                        tela.blit(txt, (j[3][0] + 6, j[3][1]))
                        j[2] = 'revelado' if revelar == 1 else 'aberto'

                if j[1] > 0 and j[2] == 'revelado':
                    clicar_com_esquerdo_em_numero(j[0])



            elif revelar == 0:
                if j[2] != 'revelado':
                    if j[2] == 'interrogação': #VERIFICA SE O STATUS ESTÁ COMO INTERROGAÇÃO (2)
                        pg.draw.rect(tela, CINZA_ESCURO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
                        pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
                        j[2] = 'oculto'
                    else:
                        txt = fonte.render('?', True, VERMELHO_ESCURO)
                        tela.blit(txt, (j[3][0]+6, j[3][1]))
                        j[2] = 'interrogação'


            validar_vitoria()


            primeira_jogada = False
            break

casas_reveladas = []

def remover_duplicatas(lista):
    nova_lista = []
    global contador_de_casas

    for i in lista:
        if i not in nova_lista and i not in casas_reveladas:
            nova_lista.append(i)
            casas_reveladas.append(i)
            contador_de_casas+=1
    return nova_lista


def mostrar_casas_vazias():
    for h, i in dic.items():
        if i[1] == 0 and i[2] == 'revelado':
            print(h, i)

def revelar_casas_vazias():
    # c, d = 0, 0
    casas = []
    for _ in range(LINHAS*COLUNAS//2):
        for i in dic.values():
            if i[2] == 'revelado' and i[1] == 0:

                casas.extend(casas_ao_redor(i[0]))
                casas = remover_duplicatas(casas)

                for i in casas:
                    j = dic[f'{i[0]},{i[1]}']
                    pg.draw.rect(tela, CINZA_CLARO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
                    pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
                    valor_do_campo = ' ' if str(j[1]) == '0' else str(j[1])
                    txt = fonte.render(valor_do_campo, True, PRETO)
                    tela.blit(txt, (j[3][0] + 6, j[3][1]))
                    j[2] = 'revelado'

def clicar_com_esquerdo_em_numero(pos):
    linha = pos[0]
    coluna = pos[1]
    valor = dic[f'{linha},{coluna}'][1]

    casas_proximas = []
    valores_proximos = []

    cont = 0

    #VERIFICAR SE A QUANTIDADE DE INTERROGAÇÕES É IGUAL AO NÚMERO NA CASA
    for i in casas_ao_redor(pos):
        if dic[f'{i[0]},{i[1]}'][2] == 'interrogação':
            cont += 1
        elif dic[f'{i[0]},{i[1]}'][2] == 'oculto':
            casas_proximas.append(i)
            valores_proximos.append(dic[f'{i[0]},{i[1]}'][1])

    if cont != valor:
        return 0

    #SE UMA DELAS TIVER BOMBA, ACIONAR EXPLOSÃO

    if '*' in valores_proximos:
        explosao()
        return 0


    #REVELAR TODAS AS CASAS QUE NÃO TENHAM INTERROGAÇÃO
    for i in casas_proximas:
        j = dic[f'{i[0]},{i[1]}']
        pg.draw.rect(tela, CINZA_CLARO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado))
        pg.draw.rect(tela, PRETO, (j[3][0], j[3][1], largura_do_quadrado, largura_do_quadrado), 1)
        valor_do_campo = ' ' if str(j[1]) == '0' else str(j[1])
        txt = fonte.render(valor_do_campo, True, PRETO)
        tela.blit(txt, (j[3][0] + 6, j[3][1]))
        j[2] = 'revelado'

    if 0 in valores_proximos:
        revelar_casas_vazias()


def validar_primeira_jogada():
    jogar()





if __name__=='__main__':
    while True:

        pg.display.update()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                exit()

            if e.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if e.button == 1:

                    selecionar_casa(pos, True)


                if e.button == 3:
                    selecionar_casa(pos, False)
