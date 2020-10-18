from animal import Animal
from gerenciarEspecie import GerenciarEspecie

class GerenciarAnimal:
    def criarAnimal(lista_de_especies, animal):
        x = True

        if(type(animal) != bool):
            id = animal.id
            especie = animal.especie
        else:
            id = input("Digite o ID do animal: ")
            while (x == True):
                especie = input("Digite a espécie do animal ou 0 para sair: ")
                if (especie == '0'):
                    return False

                for e in lista_de_especies:
                    if (especie == e.especie):
                        especie = e
                        x = False

                if(x == False):
                    continue
                else:
                    print("Esta espécie não existe. Lista de espécies existentes: ")
                    GerenciarEspecie.exibirEspecie(lista_de_especies)
                    print("Tente novamente.")

        idade = input("Digite a idade do animal: ")
        peso = input("Digite o peso do animal: ")
        altura = input("Digite a altura do animal: ")
        status = input("Digite o status do animal: ")

        return (Animal(id, especie, idade, peso, altura, status))

    def exibirAnimal(lista_de_animais):
        if (len(lista_de_animais) == 0):
            print("Ainda não existem animais inseridos.")
        for a in lista_de_animais:
            print(a)

    def removerAnimal(lista_de_animais):
        GerenciarAnimal.exibirAnimal(lista_de_animais)
        id = int(input('Digite o ID do animal que deseja remover: '))
        resposta = GerenciarAnimal.procurarAnimal(id, lista_de_animais)
        if (type(resposta) == int):
            lista_de_animais.pop(resposta)
        else:
            print(resposta)

    def editarAnimal(lista_de_animais, lista_de_especies):
        GerenciarAnimal.exibirAnimal(lista_de_animais)
        id = int(input('Digite o ID do animal que deseja editar: '))
        resposta = GerenciarAnimal.procurarAnimal(id, lista_de_animais)
        if (type(resposta) == int):
            animal = lista_de_animais[resposta]
            lista_de_animais.pop(resposta)
            lista_de_animais.insert(resposta, GerenciarAnimal.criarAnimal(lista_de_especies, animal))
        else:
            print(resposta)

    def procurarAnimal(id, lista_de_animais):
        x = 0
        for e in lista_de_animais:
            animalid = int(e.id)
            if (animalid == id):
                return (x)
            x += 1
        return "Não existe animal com este ID."
