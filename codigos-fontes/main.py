import funcoes
repetir = True

while repetir == True:
    opcao = funcoes.menuPrincipal()

    if opcao == 2:
        repetir = funcoes.pegadaCarbono()

    elif opcao == 3:
        repetir = funcoes.cadastroOng()

    elif opcao == 4:
        repetir = funcoes.mostrarOgns()
    if opcao == 5:
        repetir = funcoes.outros()
