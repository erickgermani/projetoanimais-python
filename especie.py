class Especie:
    def __init__(self, id, especie):
        self.id = id
        self.especie = especie

    def __str__(self):
        return f"#{self.id} - {self.especie}"

    def retornar_especie(self):
        return especie
