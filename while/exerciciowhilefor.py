def percorredor():
    print("n pratica do for: ")
    for contador in range(1,18):
        print(f" é menor de idade: {contador}")
        if(contador == 18):
            break

    print(contador)

def contador_ate_cinco():
    print("pratica do while: ")
    contador = 1
    while contador <= 5:
        print(contador)
        contador +=1
