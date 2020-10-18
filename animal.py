class Animal:
    def __init__(self, id, especie, idade, peso, altura, status):
        self.id = id
        self.especie: especie = especie
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.status = status

    def __str__(self):
        return f"[#{self.id}, especie: {self.especie.especie}.\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\nStatus: {self.status}]"