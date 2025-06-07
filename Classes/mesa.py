import random
from Classes.player import Jogador
class Maquina(Jogador):
    def __init__(self, pontos_iniciais):
        super().__init__('Máquina', pontos_iniciais)
        self.palpite = 0
        self.pedras_na_mao = 3
        self.reveladas = 0

    def revelar_pedras(self):
        self.reveladas = random.randint(0, 3)
    
    def fazer_palpite(self):
        self.palpite = random.randint(0, 6)

    def perder_pontos(self, valor):
        super().perder_pontos(valor)

    def ganhar_pontos(self, valor):
        super().ganhar_pontos(valor)
