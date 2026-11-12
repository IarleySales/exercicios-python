def mostrar_acoes():
    print("---- Acoes do Personagem ----")
    print("1 - Correr (gasta 20 de energia)")
    print("2 - Pular muro (gasta 35 de energia)")
    print("3 - Descansar")
    opcao = int(input("O que voce quer fazer? "))
    return opcao

def jogar():
    energia = int(input("Quanto de energia seu personagem tem agora? "))
    acao = mostrar_acoes()

    if energia >= 20 and acao == 1:
        print("Voce correu! Sobrou", energia - 20, "de energia.")
    elif energia >= 35 and acao == 2:
        print("Voce pulou o muro! Sobrou", energia - 35, "de energia.")
    elif acao == 3:
        print("Voce descansou e continua com", energia, "de energia.")
    elif acao > 3 or acao < 1:
        print("Essa opcao nao existe")
    else:
        print("Energia insuficiente pra fazer isso")

jogar()