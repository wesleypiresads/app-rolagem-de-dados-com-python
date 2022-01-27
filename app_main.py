import random

def parse_input(input_string):
    if input_string.strip() in {'1', '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print('Por favor, entre com o numero entre 1 e 6')
        raise SystemExit(1)

def roll_dice(numero_dados):
    #function retorna uma lista de inteiros
    roll_results = []
    #Procurando uma lista de inteiros em um intervalo de 1 a 6
    for _ in range(numero_dados):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def gerar_diagrama_dados(dados_valor):

    lados_dados = []
    for valor in dados_valor:
        lados_dados.append(DICE_ART[valor])

    lados_dados_linha = []
    for linha_idx in range(DIE_HEIGHT):
        linha_componentes = []
        for die in lados_dados:
            linha_componentes.append(die[linha_idx])
        linha_string = DICE_FACE_SEPARATOR.join(linha_componentes)
        lados_dados_linha.append(linha_string)

    width = len(lados_dados_linha[0])
    diagrama_header = 'RESULTS'.center(width, '~')

    lados_dados_diagrama = '\n'.join([diagrama_header] + lados_dados_linha)
    return lados_dados_diagrama

# Diagrama de ASCII (Esse diagrama foi copiado para facilitar o desenvolvimento)
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DICE_FACE_SEPARATOR = ' '

# Validando a entrada de dados do usuario
entrada_numero_dados = input('Quantos dados você quer jogar escolha de [1 a 6] ')
# Função (parse_input) Pegando a entrada do usuário como string verificando se inteiro e retornando inteiro
numero_dados = parse_input(entrada_numero_dados)

roll_results = roll_dice(numero_dados)

# Linha para testar o aplicativo durante o desenvolvimento
#print(roll_results)