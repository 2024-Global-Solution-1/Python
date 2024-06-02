import funcoes
repetir = True

while repetir == True:
    opcao = funcoes.menuPrincipal()

    if opcao == 2:
        repetir = funcoes.pegadaCarbono()

    if opcao == 5:
        repetir = funcoes.outros()
