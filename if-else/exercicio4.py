def pegar_modo():
    print("1 - Jogar (gasta 30%)")
    print("2 - Ver video (gasta 15%)")
    print("3 - Deixar bloqueado")
    return int(input("Escolha o que fazer: "))

def celular():
    bateria = int(input("Quantos % de bateria tem? "))
    modo = pegar_modo()

    if bateria >= 30 and modo == 1:
        print("Jogando... ficou com", bateria - 30, "%")
    elif bateria >= 15 and modo == 2:
        print("Vendo video... ficou com", bateria - 15, "%")
    elif modo == 3:
        print("Tela bloqueada, ainda tem", bateria, "%")
    else:
        print("Acabou a bateria muito rápido")

celular()