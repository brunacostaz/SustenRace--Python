import random

#Função responsável por procurar um item dentro de uma lista. Caso ele pertença a ela, retorna verdadeiro. Se não existir na lista, retorna falso
def meu_in(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

#Função que forçará o usuário a digitar uma das opções solicitadas.
# Se para responder uma pergunta, peço 'sim' ou 'nao', e o usuário digita 'quero', o sistema não deixará ele progredir. Deverá digitar o que foi solicitado
def forca_escolha(lista,msg):
    escolha = input(msg)
    while not meu_in(lista, escolha):
        print('Opção inválida!')
        escolha = input(msg)
    return escolha

#Função responsável por verificar se o input do user é um número
#Se for, irá converter a entrada em string para int
#se não for, forçará o usuário a digitar apenas números
def verificar_num(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Digite somente números!')
        num = input(msg)
    num = int(num)
    return num

#Essa função é bem similar com as de cima
#Nela, será verificada duas coisas ao mesmo tempo: se o input é um número e se está dentro de um intervalo pré-determinado
#Uma aplicação dela no main é no momento em que o usuário escolhe a quantidade de corridas que deseja ver
#Se ele digitar mais que 8 (total de itens na lista no momento) ficaria sem sentido a criaçao de uma tabela com bpm de uma corrida que não existe
#Ao mesmo tempo, se ele digitar qualquer coisa que nao seja um número, não terá como criar os gráficos
def verificar_num_intervalo(msg,min,max,erro):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            if num >= min and num <= max:
                return num
            else:
                print(erro)
        else:
            print('Digite somente números!')

#Função responsável por gerar números aleatórios, através da biblioteca random
# para simular a captação de dados dos batimentos cardíacos que será feita pela implementação em arduino
#delimitei um valor mínimo, de 60 bpm, e um valor máximo, de 120 bpm, para que os valores gerados sejam logicos com a quantidade de bpm
def gerar_batimentos(num):
    valor_min = 60
    valor_max = 120
    heartBeat = []
    for i in range(num):
        batimento = random.randint(valor_min, valor_max)
        #Aqui ele adicionará na lista heartBeat para poder percorrer esses valores e gerar os gráficos para cada corrida
        heartBeat.append(batimento)
    return heartBeat

#Função super simples para substituir um dado dentro de uma lista, sem afetar a ordem dos indices de cada elemento
def substituir_dado(lista,indice,novo_dado):
    lista[indice] = novo_dado
