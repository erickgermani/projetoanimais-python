from gerenciarEspecie import GerenciarEspecie
from gerenciarAnimal import GerenciarAnimal

def encerrar():
    return print("O programa foi encerrado.")

lista_de_especies = []
lista_de_animais = []
continuar = True
print("Bem-vindo ao sistema de gerenciamento de animais.\nO que deseja fazer?")
while(continuar == True):
    print("Menu: ")
    print("1- Ver lista de espécies | 2- Ver lista de animais | 3- Adicionar espécie | 4- Adicionar animal | 5- Remover espécie | 6- Remover animal | 7- Editar animal 0- Encerrar")
    print("Opção: ")
    escolha = int(input())

    if(escolha == 1):
        GerenciarEspecie.exibirEspecie(lista_de_especies)

    elif(escolha == 2):
        GerenciarAnimal.exibirAnimal(lista_de_animais)

    elif(escolha == 3):
        lista_de_especies.append(GerenciarEspecie.criarEspecie())

    elif(escolha == 4):
        lista_de_animais.append(GerenciarAnimal.criarAnimal(lista_de_especies, animal = False))

    elif (escolha == 5):
        GerenciarEspecie.removerEspecie(lista_de_especies, lista_de_animais)

    elif (escolha == 6):
        GerenciarAnimal.removerAnimal(lista_de_animais)

    elif (escolha == 7):
        GerenciarAnimal.editarAnimal(lista_de_animais, lista_de_especies)


    elif(escolha == 0):
        continuar = False
        encerrar()

    else:
        print("A opção escolhida não existe. Deseja tentar novamente ou encerrar?")
        print("Digite {0} para encerrar e qualquer outra tecla para continuar: ")
        escolha = int(input())
        if(escolha == 0):
            continuar = False
            encerrar()