from especie import Especie

class GerenciarEspecie:
    def criarEspecie():
        id = input("Digite o ID da espécie: ")
        especie = input("Digite o nome da espécie: ")
        return (Especie(id, especie))

    def exibirEspecie(lista_de_especies):
        if (len(lista_de_especies) == 0):
            print("Ainda não existem espécies inseridas.")
        for e in lista_de_especies:
            print(e)

    def removerEspecie(lista_de_especies, lista_de_animais):
        GerenciarEspecie.exibirEspecie(lista_de_especies)
        id = int(input('Digite o ID da espécie que deseja remover: '))
        resposta = GerenciarEspecie.procurarEspecie(id, lista_de_especies)
        if(type(resposta) == int):
            lista_de_remocao = []
            x = 0
            for a in lista_de_animais:
                if(a.especie == lista_de_especies[resposta]):
                    lista_de_remocao.append(x)
                x += 1
            for r in lista_de_remocao:
                lista_de_animais.pop(r)
            lista_de_especies.pop(resposta)
        else:
            print(resposta)

    def procurarEspecie(id, lista_de_especies):
        x = 0
        for e in lista_de_especies:
            especieid = int(e.id)
            if (especieid == id):
                return (x)
            x += 1
        return "Não existe espécie com este ID."


