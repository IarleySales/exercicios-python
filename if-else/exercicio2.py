def dinheiros():

    dinheiro = int(input("Digite a quantidade de dinheiro que você tem: "))
    
    print(dinheiro)
    print("========Loja========")
    print("1- Abobora custa 2 reais.")
    print("2- Cenoura custa 3 reais")
    print("3- Não comprar")
    escolha = int(input("Escolha o que você deseja comprar: "))

    if dinheiro > 2 and escolha == 1:
        print("Você comprou a abobora", dinheiro - 2, "reais restantes.")
    elif dinheiro > 3 and escolha == 2:
        print("Você comprou a cenoura", dinheiro - 3, "reais restantes.")
    elif dinheiro > 0 and escolha == 3:
        print("Você não comprou nada, você tem", dinheiro, "reais restantes.")
    else:
        print("Você não tem dinheiro suficiente para comprar o item.")


dinheiros()