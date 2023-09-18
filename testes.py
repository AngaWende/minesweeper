# from random import randint
# numero_de_casas = 10
# tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, '*', 0, 0, 0, 0, 0, 0],
# ['*', 0, 0, 0, 0, 0, 0, 0, 0, '*'],
# [0, 0, 0, 0, 0, 0, 0, '*', 0, 0],
# [0, '*', 0, 0, 0, 0, '*', 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, '*', 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, '*', 0, 0, 0],
# ['*', 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ['*', 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# # for linha in tabuleiro:
# #     for coluna in linha:
# #         if coluna == '*':
# #             print(tabuleiro[linha][coluna])
#
# x = '13'
# y = '43'
# locais_das_bombas = ['13', '23', '08']
#
#
# def casas(linha, coluna):
#
#     lin = linha
#     col = coluna
#     campos = []
#
#
#     if lin -1 >= 0 and col-1 >= 0:
#         campos.append([lin-1, col-1])
#
#     if lin -1 >= 0 and col == col:
#         campos.append([lin-1, col])
#
#     if lin -1 >= 0 and col +1 < numero_de_casas:
#         campos.append([lin-1, col+1])
#
#     if col - 1 >= 0 and lin == lin:
#         campos.append([lin, col-1])
#
#     if col +1 < numero_de_casas:
#         campos.append([lin, col+1])
#
#     if lin +1 < numero_de_casas and col -1 >= 0:
#         campos.append([lin+1, col-1])
#
#     if lin +1 < numero_de_casas and col == col:
#         campos.append([lin+1, col])
#
#     if lin +1 < numero_de_casas and col +1 < numero_de_casas:
#         campos.append([lin+1, col+1])
#
#     print(campos)
#
#
#
# for l in tabuleiro:
#     print(l)
#
#
# while True:
#
#     coordenadas = input('coordenadas')
#
#     casas(int(coordenadas[0]), int(coordenadas[1]))
#
#
#

# Tamanho do tabuleiro
largura = 8
altura = 8

# Crie um tabuleiro vazio
tabuleiro = [[' ' for _ in range(largura)] for _ in range(altura)]

# Função para revelar células vazias interconectadas
def revelar_vazias(tabuleiro, x, y):
    # Verifique os 8 vizinhos ao redor da célula atual
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Calcule as coordenadas do vizinho
            nx, ny = x + dx, y + dy
            # Verifique se o vizinho está dentro dos limites do tabuleiro
            if 0 <= nx < largura and 0 <= ny < altura:
                # Verifique se o vizinho ainda não foi revelado e não contém uma bomba
                if tabuleiro[ny][nx] == ' ':
                    # Marque a célula como revelada
                    tabuleiro[ny][nx] = '0'  # Ou qualquer outro caractere para indicar que está vazia
                    # Recursivamente, revele os vizinhos dessa célula
                    revelar_vazias(tabuleiro, nx, ny)

# Exemplo de uso: revelar a célula (3, 3)
tabuleiro[3][3] = '0'  # Suponha que '0' representa uma célula vazia
print(revelar_vazias(tabuleiro, 3, 3))
