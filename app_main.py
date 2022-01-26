# Validando a entrada de dados do usuario
entrada_numero_dados = input('Quantos dados você quer jogar escolha de [1 a 6] ')
# Função (parse_input) Pegando a entrada do usuário como string verificando se inteiro e retornando inteiro
numero_dados = parse_input(entrada_numero_dados)

def parse_input(input_string):

    if input_string.strip() in {'1', '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print('Por favor, entre com o numero entre 1 e 6')
        raise SystemExit(1)