
class Mesa:
    def __init__(self, pontos_iniciais):
        self.pontos = pontos_iniciais
        self.pedras_na_mao = 6
        self.reveladas = 0

    def revelar_pedras(self):
        import random
        self.reveladas = random.randint(1, 6)

    def perder_pontos(self, valor):
        if valor > self.pontos:
            self.pontos = 0
        else:
            self.pontos -= valor

    def ganhar_pontos(self, valor):
        self.pontos += valor

    def mostrar_estado(self):
        print(f"Pontos: {self.pontos}")
        print(f"Reveladas: {self.reveladas}")
        