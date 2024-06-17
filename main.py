#Importando biblioteca matplolib (para criar gráficos)
#E importando todas as funções e listas dos outros arquivos

import matplotlib.pyplot as plt #'as' faz uma abreviaçção do nome a ser chamado da biblioteca
from funcoes import *
from listas import *

print('\n------------------------------------------------------------------------------------------------------')
print('\n                                   Seja muito bem-vindo à SustenRace!')

#Exibição do batimento cardíaco médio das pessoas nas últimas corridas

#Para exibir isso, utilizamos a biblioteca random para gerar números aleatórios entre 60 e 120 (está no arquivo de funções)
#Isso representará os batimentos cardíacos que estariam sendo captados pela nossa implementação em arduino (o relógio com sensor de bpm).
#Além disso, criaremos um gráfico para visualizar esses dados com o auxilio da biblioteca matplolib.py

print('\n---------------------------------------------- Emoção da Corrida ----------------------------------------------\n')
print('Confira os batimentos cardíacos do público nas últimas corridas da Fórmula E!\n')
#O valor informado pelo usuário precisa ser correspondente ao total de corridas cadastradas. No momento, há 8 corridas, portanto, ele só poderá ver dentro desse intervalo
qnt_batimento = verificar_num_intervalo(f'Deseja ver a emoção de quantas das últimas corridas? (ocorreu {len(corridas)} até o momento)\n-> ',1,len(corridas),f'Nessa temporada de 2024 ocorreram apenas {len(corridas)} corridas.\nPortanto, você só conseguirá ver a emoção dessa quantidade.')
#Acionamento da função que usa o random para gerar valores aleatórios, simulando a média de batimentos do público para a quantidade de corrida que o usuário pediu
bpm = gerar_batimentos(qnt_batimento)

#criação do gráfico de barras, a partir de um eixo X e Y

#Eixo X será a quantidade de corridas que o usuário deseja ver. Se ele quer ver as últimas 5 corridas, será criado 5 barras
eixoX = []
#É necessário um for para percorrer o range do número informado pelo user
for i in range(qnt_batimento):
      eixoX.append(i+1)

#O eixoY é o valor dos bpm gerados pelo random (geração de números aleatórios dentro do intervalo de 60 a 120 bpm)
eixoY = bpm

#tanto o eixo X quanto o Y são listas, a partir da correlação de seus indices, eles formaram um gráfico de barras para cada 'corrida'
#dessa forma, a corrida 1 terá uma média de bpm de 90 (gerada pelo random na função, por exemplo), pois ambos estão no indice 0, e assim por diante

#Criação de títulos para o gráfico, o eixo X e o eixo Y, respectivamente
titulo = f'Batimento cardíaco médio das últimas {qnt_batimento} corridas'
titleX = 'Corridas'
titleY = 'BPM'

#Atribuição dos títulos acima para as regiões em que devem aparecer
plt.title(titulo)
plt.xlabel(titleX)
plt.ylabel(titleY)

#Criação do Gráfico de tabelas:
# .bar(): cria o gráfico de barras a partir de uma eixo X e um eixo Y
# label: cria uma legenda:
#           xlabel e ylabel (como feito acima) cria a legenda para cada eixo.
#           label = corridas[i] cria uma legenda descritiva para cada barra criada (como feito abaixo)
# .legend(): adiciona as legendas criadas na tabela
# .show(): executa o gráfico

#Esse for é responsável pela criação das legendas de cada barra a partir da quantidade de corridas que o usuário deseja ver
#Ou seja, as corridas foram colocas na lista corridas em ordem decrescente (da última feita a primeira feita em 2024)
# o comando 'min' garante que a repetição do for a atribuição dos indices serão somente para a quantidade pedida pelo usuário e dentro dos indices existentes
#dessa forma, evita que ocorra o erro do for repetir mais vezes do que o pedido, ao mesmo tempo em que evita ele associar a um indice inesxistente

for i in range(min(qnt_batimento, len(corridas))):
    bar = plt.bar(eixoX[i], eixoY[i], label = corridas[i])

    #Aqui será feita a criação de uma legenda em cima de cada barra, para mostrar o valor exato "batimento" medido
    #armazenamos o valor do plt.bar na variável bar, que é um objeto retangular.
    #por isso, é usado rect como variável para adicionar os valores de cada barra, pois rect é a abreviação para rectangle

    for rect in bar:
        #armazena o valor da altura da barra trabalhada no momento
        height = rect.get_height()
        #Cria o texto acima da barram a partir do cálculo da metade entre a largura e a posição de x, a altura da barra e o alinhamento
        # do texto para o centro e examente acima do topo da barra
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')

#Legend(): adiciona as legendas no gráfico
#loc = 'upper left': define a referência do posicionamento da caixa, superior esquerdo
#bbox_to_anchor = (1,1): ajusta a posição da legenda, sendo x e y. Ambos variam de 0 a 1
#       para x, 0 é extrema esquerda e 1 extrema direita
#       para y, 0 é parte inferior e 1 é parte superior
#Dessa forma, a legenda é posicionada do lado de fora do gráfico, no canto superior direito
plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))

#Ajusta o tamanho da imagem, para evitar que a legenda fique cortada
plt.subplots_adjust(right=0.60)
plt.show()

print('\n------------------------------------------------------------------------------------------------------\n')
cadastro = []
tem_conta = False
envios = False
ideias_melhorias = []
while True:
    # Realização do cadastro de usuário
    # Só aparecerá esse if para ele caso ele não tenha cadastrado (tem_conta estará False indicando isso)
    #Para acessar o perfil e enviar ideias de melhoria, é necessário ter cadastro
      if tem_conta == False:
            cadastrar = forca_escolha(SimNao,'\nDeseja realizar o seu cadastro? (sim/nao)')
            #Cadastro do usuário
            if cadastrar == SimNao[0] or cadastrar == SimNao[1]:
                nome = input('Digite o seu primeiro nome: ')
                cadastro.append(nome) #Insersão dos dados na lista de cadastro
                sobrenome = input('Digite o seu sobrenome: ')
                cadastro.append(sobrenome)
                email = input('Informe o seu email: ')
                cadastro.append(email)
                cpf = verificar_num('Informe o seu CPF (digite somente números)')
                cadastro.append(cpf)
                nasc_dia = verificar_num('Em que dia você nasceu?')
                cadastro.append(nasc_dia)
                nasc_mes = verificar_num('Em que mês você nasceu? ')
                cadastro.append(nasc_mes)
                nasc_ano = verificar_num('Em que ano você nasceu? ')
                cadastro.append(nasc_ano)
                tel = verificar_num('Informe o seu telefone (só números) ')
                cadastro.append(tel)

                print('\nVerifique os dados informados:\n')
                print(f'1.Nome: {cadastro[0]}\n2.Sobrenome: {cadastro[1]}\n3.Email: {cadastro[2]}\n4.CPF: {cadastro[3]}\n'
                      f'5.Data de Nascimento: {cadastro[4]} / {cadastro[5]} / {cadastro[6]}\n6.Telefone: {cadastro[7]}')
                validar = forca_escolha(SimNao,'\nOs dados informados estão corretos? (sim/nao)\n-> ')

                #verificação dos dados e correção caso algum esteja incorreto
                while validar == SimNao[2] or validar == SimNao[3] or validar == SimNao[4] or validar == SimNao[5]:
                    #Solicitação para o user digitar o número correspondente ao dado que está incorreto
                      iErrado = verificar_num_intervalo('Digite o número correspondente ao item que está incorreto: ',0,len(cadastro),'Digite somente de 1 a 6.')
                      #Como não foi apresentado com o indice, é necessário realizar esse mapeamento para acessar o indice correto
                      if iErrado == 1 or iErrado == 2 or iErrado == 3:
                          iErrado -= 1
                          dadoCerto = input(f'Informe o dado novo: ')
                      else:
                          if iErrado == 4:
                               iErrado = 3
                          elif iErrado == 5:
                               iErrado = verificar_num_intervalo('\nPara alterar o dia, digite 4\n'
                                                              'Para alterar o mês, digite 5\n'
                                                              'Para alterar o ano, digite 6\n-> ', 4, 6,
                                                              'Digite somente 4,5 ou 6')
                          else:
                              iErrado = 7
                          dadoCerto = verificar_num('Informe o dado novo: ')
                      #através dessa função, será realizada a substituição do dado errado para o correto, informado pelo user
                      substituir_dado(cadastro,iErrado,dadoCerto)
                      print(f'\n1.Nome: {cadastro[0]}\n2.Sobrenome: {cadastro[1]}\n3.Email: {cadastro[2]}\n4.CPF: {cadastro[3]}\n'
                          f'5.Data de Nascimento: {cadastro[4]} / {cadastro[5]} / {cadastro[6]}\n6.Telefone: {cadastro[7]}')
                      outro_erro = forca_escolha(SimNao,'\nPossui mais algum dado incorreto? (sim/nao)')
                    #O loop se repete caso haja mais algum erro, e finaliza caso tudo esteja certo
                      if outro_erro ==  SimNao[2] or outro_erro == SimNao[3] or outro_erro == SimNao[4] or outro_erro == SimNao[5]:
                          break
                print(f'\nCadastro feito com sucesso!!! Seja muito bem-vindo(a) {cadastro[0]}\n')
                tem_conta = True
    #Se o usuário já tiver cadastro e solicitar visitar o menu novamente, ele virá direto para cá.
    #mas caso o user não tenha cadastro, ele primeiro passará pelo if acima.
      print('\n---------------------------------------------- Menu ----------------------------------------------\n')
      for i in range(len(menu)):
        print(f'{i}. {menu[i]}')
      print('\n------------------------------------------------------------------------------------------------------\n')
      navegar = verificar_num('Deseja navegar em qual seção? Informe o número correspondente\n-> ')
      print(f'---------------------------------------------- {menu[navegar]} ----------------------------------------------')

      #Essa seção irá direcionar o usuário para a "página" que ele deseja acessar
      if menu[navegar] == menu[0]:
           #se houver cadastro, ele entrará nesse if, onde mostra o histórico de suas ideias (caso tenha alguma) e seus dados cadastrais (com opção de atualizá-los)
            if tem_conta == True:
                print(f'\n Olá {cadastro[0]}!\n')
                print('\n---------------------------------------------- Minhas Ideias ----------------------------------------------\n')
                if envios == False:
                      print('Você ainda não enviou ideias de melhoria para a gente :(\n'
                            '\nConfiamos no seu potencial e a Fórmula E pode ter muitas melhorias com a sua criação\n'
                            'Portanto, não perca tempo, acesse a seção "Criar minhas ideias inovadoras" e envie suas ideias!\n')
                      print('\n------------------------------------------------------------------------------------------------------\n')
                else:
                      print(f'Você possui um total de {len(ideias_melhorias)} ideias enviadas.\n')
                      for i in range(len(ideias_melhorias)):
                            print(f'Ideia {i+1}:\n\n{ideias_melhorias[i]}\n')
                      print('\n------------------------------------------------------------------------------------------------------\n')

                config = forca_escolha(SimNao,'\nDeseja abrir as configurações para ver seus dados cadastrais? (sim/nao)\n-> ')
                if config == SimNao[0] or config == SimNao[1]:
                      print(f'\n1.Nome: {cadastro[0]}\n2.Sobrenome: {cadastro[1]}\n3.Email: {cadastro[2]}\n4.CPF: {cadastro[3]}\n'
                            f'5.Data de Nascimento: {cadastro[4]} / {cadastro[5]} / {cadastro[6]}\n6.Telefone: {cadastro[7]}')
                      mudar = forca_escolha(SimNao,'\nDeseja atualizar algum dado? (sim/nao) ')
                      if mudar == SimNao[0] or mudar == SimNao[1]:
                          while True:
                              atual = verificar_num_intervalo('\nDigite o número correspondente ao item que você deseja atualizar: ', 0, len(cadastro),'Digite somente de 1 a 6.')
                              if atual == 1 or atual == 2 or atual == 3:
                                    atual -= 1
                                    dadonovo = input(f'Informe o dado novo: ')
                              else:
                                  if atual == 4:
                                      atual = 3
                                  elif atual == 5:
                                      atual = verificar_num_intervalo('\nPara alterar o dia, digite 4\n'
                                                                      'Para alterar o mês, digite 5\n'
                                                                      'Para alterar o ano, digite 6\n-> ',4,6,'Digite somente 4,5 ou 6')
                                  else:
                                      atual = 7
                                  dadonovo = verificar_num('Informe o dado novo: ')

                              substituir_dado(cadastro, atual, dadonovo)
                              print(f'\n1.Nome: {cadastro[0]}\n2.Sobrenome: {cadastro[1]}\n3.Email: {cadastro[2]}\n4.CPF: {cadastro[3]}\n'
                                  f'5.Data de Nascimento: {cadastro[4]} / {cadastro[5]} / {cadastro[6]}\n6.Telefone: {cadastro[7]}')

                              outro_dado = forca_escolha(SimNao, '\nDeseja atualizar mais algum dado? (sim/nao)')
                              if outro_dado == SimNao[2] or outro_dado == SimNao[3] or outro_dado == SimNao[4] or outro_dado == SimNao[5]:
                                  break
            else:
            #Se o user nao tiver cadastro, ele cairá direto aqui, e o continue voltará a execução para o pedido de cadastro
                print('\nVocê ainda não possui cadastro :(\n')
                print('------------------------------------------------------------------------------------------------------\n')
                continue
            print('\n------------------------------------------------------------------------------------------------------')
    #nessa seção, será mostrado os detalhes dos batimentos cardíacos de cada corrida registrada
    #além disso, mostrará um gráfico identico ao mostrado no inicio da execução
      elif menu[navegar] == menu[1]:
            print(f'\nDetalhes dos batimentos cardíacos:\n')
            for i in range(len(corridas)):
                  lista_bpm = gerar_batimentos(1)
                  print_formatado = ''.join(map(str, lista_bpm))
                  print(f'{corridas[i]} -> BPM médio: {print_formatado} bpm')
                  if lista_bpm[0] < 80:
                        print('Essa corrida foi menos emocionante!\n')
                  elif lista_bpm[0] < 100:
                        print('Essa corrida foi muito emocionante!\n')
                  else:
                        print('É EMOÇÃO QUE VOCÊ QUER? POIS É ISSO QUE TERÁ!\n')
            qnt_batimento = verificar_num_intervalo(f'Deseja ver a emoção de quantas das últimas corridas? '
                                                    f'(ocorreu {len(corridas)} até o momento)\n-> ', 1,len(corridas),
                                                    f'Nessa temporada de 2024 ocorreram apenas {len(corridas)} corridas.\nPortanto, '
                                                    f'você só conseguirá ver a emoção dessa quantidade.')
            #Criação do gráfico de batimentos cardíacos, identico ao feito no inicio da execução do código
            bpm = gerar_batimentos(qnt_batimento)

            eixoX = []
            for i in range(qnt_batimento):
                eixoX.append(i + 1)
            eixoY = bpm

            titulo = f'Batimento cardíaco médio das últimas {qnt_batimento} corridas'
            titleX = 'Corridas'
            titleY = 'BPM'

            plt.title(titulo)
            plt.xlabel(titleX)
            plt.ylabel(titleY)

            for i in range(min(qnt_batimento, len(corridas))):
                bar = plt.bar(eixoX[i], eixoY[i], label=corridas[i])
                for rect in bar:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')

            plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
            plt.subplots_adjust(right=0.60)
            plt.show()

            plt.show()
            print('\n------------------------------------------------------------------------------------------------------\n')
      #Nessa seção, o user conseguirá enviar as ideias que ele tem para melhorar os carros da Mahindra, caso ele tenha cadastro
      #essas ideias serão registradas no perfil do usuário e serão mostradas a ele caso ele acesse o perfil
      #Isso é acumulativo, logo tudo estará sendo armazenado, simulando um banco de dados
      else:
            if tem_conta == False:
                print('\nPara nos enviar suas ideias, é necessário realizar o seu cadastro!')
                continue
            ideia = input('\nVocê teve alguma ideia inovadora? Conte para a gente:\n-> ')
            ideias_melhorias.append(ideia)
            print('\nIdeia enviada com sucesso!!\n\nCaso a Mahindra se interesse pela sua ideia, você receberá um email de notificação\n'
                  'Nesse email nós também pediremos o seu pix para realizarmos o deposito da sua recompensa em dinheiro.\n'
                  'O MAIS ESPERADO: você será notificado se sua participação na implementação será parcial ou integral\n\n'
                  'ISSO MESMO! Você terá a oportunidade de trabalhar ao lado dos mecânicos e engenheiros da Mahindra, implementando sua ideia\n'
                  'Todos em busca de entretenimento sustentável! Boa sorte! :) ')
            envios = True
            while True:
                mais = forca_escolha(SimNao,'\nDeseja enviar mais alguma ideia? (sim/nao) ')
                if mais == SimNao[0] or mais == SimNao[1]:
                    ideia = input('\nDescreva sua ideias aqui!\n-> ')
                    ideias_melhorias.append(ideia)
                    continue
                break
            print('\n------------------------------------------------------------------------------------------------------\n')
      navegar = forca_escolha(navegacao,'\n\nDeseja voltar ao menu ou encerrar a navegação pelo site? (voltar ou encerrar)\n-> ')
      #Caso queira voltar ao menu, ocorrerá duas coisas:
      #    1. Se não possui cadastro, ele voltará para o inicio do while, onde é perguntado se ele deseja fazer o cadastro
      #    2. Se possui cadastro, ele será levado direto para o menu
      #Caso ele escolha encerrar a navegação, entraá nesse if com uma mensagem de agradecimento e um break do while
      if navegar == navegacao[1]:
          print('\nAgradecemos pela preferência e esperamos que a SustenRace seja muito útil para você!')
          break

