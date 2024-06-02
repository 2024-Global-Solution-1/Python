# Função de verificar se é um número
# É necessario passar o text que pede o tal número
def VerificarNum(text):
    repetirVeri = True

    while repetirVeri == True:
        try:
            var = int(input(text))
        except:
            





# Função do menu principal
def menuPrincipal():
    menu = """
    ----------------------------------------------------------------------------------
                                        BEM VINDO
                            
    [1] - Quero receber informações importantes sobre o Ôceano
    [2] - Quero Calcular minha pegada de carbono
    [3] - Sou uma ONG em prol do Ôceno e quero me cadastrar para ganhar repercussão
    [4] - Sou um Doador, me mostre algumas ONG's para doar
    [5] - Outros

    ----------------------------------------------------------------------------------"""

    print(menuPrincipal)

    msgMenu = "Digite o número correspondente com a sua opção desejada\n==> "

    opcaoMenu = input(msgMenu)
    
    return opcaoMenu


# Função da opção Outros
def outros():
    print("Entre em contato com nosso suporte por e-mail ou github;")