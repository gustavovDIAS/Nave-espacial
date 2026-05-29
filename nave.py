##Definir variaveis
combustivel=110
tripulantes=[]
##Definir funções
def viajar(): ##Gastar combustivel
    
    global combustivel
    if (combustivel>=30):
        combustivel= combustivel- 30
        print("A nave viajou com sucesso 🚀🚀")
    else:
        print("Voce está sem combustivel suficiente. Abasteça!")


def abastecer():
    print("-----------------------------------")
    global combustivel
    combustivel=110
    print("Tanque cheio! ⛽")

def stNave():
    print("----------STATUS DA NAVE-----------")
    print(f"A nave esta com {combustivel}L de combustivel")
    print(f"Os tripulantes são:{tripulantes}")
    print("-----------------------------------")


def resTrip():##Add tripulantes
    novoTripulante = input("Qual nome do novo tripulante? ")
    tripulantes.append(novoTripulante) ## inserimos
    print("Tripulante inserido com sucesso! 🚀")

##Menu 

print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
while True : #Roda para sempre
    print("\n1- Mostrar status da nave| 2- Viajar| 3- Abastecer| 4- Novo Tripulante |5-Sair")
    opcao=input("Escolha: ")
    if (opcao=="1"):
        stNave()
    elif (opcao=="2"):
        viajar()
    elif (opcao=="3"):
        abastecer()
    elif (opcao=="4"):
        resTrip()
    elif (opcao=="5"):
        print("Viagem encerrada!")
        break
