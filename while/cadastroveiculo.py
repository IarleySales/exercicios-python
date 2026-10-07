def cadastrar_veiculo():
    print("Cadastro de Veículo")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    placa = input("Digite a placa do veículo: ")
    servico = input("Qual o tipo de serviço desejado (1 - troca de óleo, 2 - alinhamento, 3 - revisão): ")

    if servico == "1":
        print(f"Serviço de troca de óleo cadastrado para o veículo {marca} {modelo} de placa {placa}.")
    elif servico == "2":
        print(f"Serviço de alinhamento cadastrado para o veículo {marca} {modelo} de placa {placa}.")
    elif servico == "3":
        print(f"Serviço de revisão cadastrado para o veículo {marca} {modelo} de placa {placa}.")
    else:
        print("Serviço não encontrado. Por favor, escolha uma opção válida.")
    return marca, modelo, placa, servico

def consulta_veiculo(): 
    marca, modelo, placa, servico = cadastrar_veiculo()

    print("Consulta de Veículo") 

    marca_consulta = input("Digite a marca do veículo para consulta:") 
    modelo_consulta = input("Digite o modelo do veículo para consulta:") 
    placa_consulta = input("Digite a placa do veículo para consulta:") 
 
    if marca_consulta == marca and modelo_consulta == modelo and placa_consulta == placa: 
        print(f"Veículo encontrado: {marca} {modelo} de placa {placa}. Está no serviço de {servico}")

        status = "em andamento"

        while status == "em andamento":
            consultar_status = input("Deseja consultar o status do serviço? (sim/nao): ")

            if consultar_status == "sim":
                print(f"O status do serviço para o veículo {marca} {modelo} de placa {placa} é: {status}.")
                break

            else:
                print("Consulta de status encerrada.")

    else: 
        print("Veículo não encontrado, verifique os dados informados.")

consulta_veiculo()