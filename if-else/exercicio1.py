idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
    
elif idade >= 14 and idade < 16:
    print("menor de idade já pode pegar ônibus sozinho")
    
elif idade >= 16:
    print("Já pode pegar ônibus sozinho")

else:
    print("Você é menor de idade")  

idade()