import classes

# Função de verificar se é um número
def VerificarNum(text, tipo = float): # É necessario passar o text que pede o tal número e o tipo de dado se é Inteiro ou Real

    repetirVeri = True
    msg = text

    while repetirVeri == True:

        if tipo == int:
            try:
                var = int(input(msg))
                repetirVeri = False
            except:
                msg = "\n\nDigite um valor que seja um número inteiro\n" + text
        else: 
            try:
                var = float(input(msg))
                repetirVeri = False
            except:
                msg = "\n\nDigite um valor que seja um número \n" + text

    return var



#Função que verifica se a resposta é S ou N
def verificarSN(text):
    respostaInvalida = True
    msg = text

    while respostaInvalida == True:
        escolha = input(msg).upper()[0]

        if escolha != "S" and escolha != "N":
            msg = "Desculpe não entendi digite um valor correto por favor (S/N)\n==> "

        else:
            respostaInvalida = False

    return escolha



# Função do menu principal
def menuPrincipal():
    menu = """
    ------------------------------------------------------------------------------------------------
                                        BEM VINDO
                            
    [1] - Quero receber informações importantes sobre o Ôceano
    [2] - Quero Calcular minha pegada de carbono
    [3] - Sou uma ONG a favor de ajudar do Ôceno e quero me cadastrar para ganhar repercussão
    [4] - Sou um Doador, me mostre algumas ONG's para doar ou apenas quero conhecer as Ong
    [5] - Outros
    [6] - Sair

    ------------------------------------------------------------------------------------------------\n\n"""

    msgMenu = "Digite o número correspondente com a sua opção desejada\n==> "
    
    respostaInvalida = True
    while respostaInvalida == True:
        print(menu)
        opcaoMenu = VerificarNum(msgMenu, int)

        if opcaoMenu > 0 and opcaoMenu < 7:
            respostaInvalida = False
        else:
            msgMenu = "\nPor favor insira um valor dentre as opções do menu\n" + msgMenu
    return opcaoMenu



# Função que exibe o submenu dentro de outras funções
def subMenu (text = "\n"):
    menu = ("-----------------------------------------" + text +
            "\nO que o senhor(a) deseja fazer agora?"+
            "\n\n[1] - Voltar para o Menu Principal"+
            "\n[2] - Finalizar Programa" + 
            "\n-----------------------------------------" )
    mensagem = "Digite aqui o valor correspondente a função desejada\n==> "
    respostaInvalida = True

    while respostaInvalida == True:
        print(menu)
        resposta = input(mensagem)

        if resposta != "1" and resposta != "2":
            mensagem = "Por favor digite algum valor correspondente com o Menu\n==> "
            
        else: 
            respostaInvalida = False

    return resposta



# Função que exibe algumas informações importantes
def informacoes ():
    arquivo = open("codigos-fontes\informacoes.txt", "r" , encoding="utf-8")
    linha = arquivo.readlines()
    
    contador = 0
    for i in range(len(linha)):
        print(linha[i])
        contador += 1
    #print(linha)
    arquivo.close()

    resposta_user = subMenu()

    if resposta_user == "1":
        return True
    else:
        return False



# Função que Calcula a pegada de Carbono de um pessoa
def pegadaCarbono():

    print("\n\nPara calcular a sua pegada de Carbono anual devemos pegar algumas informações.(Usamos a média Brasileira do fator de emissão de cada transporte)")

    #Consumo de transporte
    possuiVeiculo = verificarSN("A sua pessoa anda de veículo próprio?(S/N)\n==> ")

    if possuiVeiculo == "S":
        tipoVec = input("O seu veículo é movido a que?(Gasolina, Diesel ou Etanol)\n==> ")[0]

        if tipoVec == "G":
            fatorEmissaoCar = 2.31
        elif tipoVec == "D":
            fatorEmissaoCar = 2.68
        elif tipoVec == "E": 
            fatorEmissaoCar = 1.61

        kmMediaCar = VerificarNum("Qual a distância média anual em Km que você percorre\n==> ")
        consumoCombus = VerificarNum("Em 1 Quilômetro quantos Litros seu carro consome em média\n==> ")

        emissaoCar = fatorEmissaoCar * kmMediaCar * consumoCombus
    else: 
        emissaoCar = 0

    andouAviao = verificarSN("A sua pessoa andou de avião esse ano?(S/N)\n==> ")

    if andouAviao == "S":
        KmMediaAvi = VerificarNum("Qual a quantidade média de Km anual que você percorreu?\n==> ")
        fatorEmissaoAvi = 0.13

        emissaoAvi = KmMediaAvi * fatorEmissaoAvi
    else:
        emissaoAvi = 0

    TransporPublic = verificarSN("A sua pessoa utiliza Transporte Público?(S/N)\n==> ")

    if TransporPublic == "S":
        KmMediaPublic = VerificarNum("Qual a distância em KM média anual que o senhor percorre nos transportes Públicos")
        fatorEmissaoPublic = 0.064

        emissaoPublic = KmMediaPublic * fatorEmissaoPublic
    else:
        emissaoPublic = 0

    # Consumo em Casa
    msgKWh = "Qual a quantidade de energia que você consome na sua casa anualmente em kWh\n==> "

    kWhAnual = VerificarNum(msgKWh)

    pegadaCarbonoPessoa = emissaoPublic + emissaoAvi + emissaoCar + kWhAnual

    print(f'A sua pegada de Carbono anual é de igual a {pegadaCarbonoPessoa} KG CO2')


    resposta_user = subMenu()

    if resposta_user == "1":
        return True
    else:
        return False



# Função para cadastrar uma ONG
def cadastroOng():
    nome = input("Qual o nome da sua ONG?\n==> ")
    sigla = input("Qual a sigla da ONG?\n==> ")
    dataFund = input("Qual foi a data de fundação da ONG?\n==> ")
    missao = input("Escreve uma breve descrição da missão, visão e objetivos da ONG.\n==> ")
    ende = input("Qual o endereço em que sua ONG se encontra?\n==> ")
    email = input("Informe qual o email de contato da ONG.\n==> ")
    rede = input("Nos informe o user de uma rede social ou link\n==> ")
    web = input("Disponibilize o link do Website da ONG caso tenha\n==> ")

    ONG = classes.novaOng(nome,sigla,dataFund,missao,ende,email,rede,web)

    resposta_user = subMenu("Cadastro de ONG conclúido")

    if resposta_user == "1":
        return True
    else:
        return False



# Função para disponibilizar ONG's para possiveís doadores
def mostrarOgns():

    arquivo = open("codigos-fontes\ongs.csv", "r", encoding="utf-8")
    ongsCadastradas = []

    repetirLeitor = True
    while repetirLeitor == True:
        linhaLida = arquivo.readline()
        if linhaLida != "":
            linhaLida = linhaLida.replace("\n", "")
            listaDados = linhaLida.split(";")
            ong = {}
            ong["nome"] = listaDados[0]
            ong["missao"] = listaDados[1]
            ong["website"] = listaDados[2]

            ongsCadastradas.append(ong)
        else:
            repetirLeitor = False
    ongsCadastradas = [elemento for elemento in ongsCadastradas[1:]]
    contador = 1
    for i in ongsCadastradas:
        print(f'\nOng {contador}\n\nNome:{i["nome"]}\nMissão: {i["missao"]}\nWebsite: {i["website"]}')
        contador += 1
    arquivo.close()
    
    resposta_user = subMenu("\nEssas são as Ongs que temos Cadastradas")

    if resposta_user == "1":
        return True
    else:
        return False



# Função da opção Outros
def outros():
    print("Entre em contato com nosso suporte por e-mail ou github;")

    resposta_user = subMenu()

    if resposta_user == "1":
        return True
    else:
        return False