
class Jogador:
    def __init__(self, nome, pontos):
        self.nome = str(nome)
        self.pontos = pontos
        self.pedras_na_mao = 3
        self.palpite = 0
        self.reveladas = 0
    
    def fazer_palpite (self):
        self.palpite = int(input(f"{self.nome}, faça seu palpite: "))
        
    def revelar_pedras (self):
        self.reveladas = int(input(f"{self.nome}, quantas pedras você quer revelar? (0 a 3): "))
        if self.reveladas < 1 or self.reveladas > 6:
            print("Valor inválido. Tente novamente.")
            self.revelar_pedras()
    
    def perder_pontos (self, valor):
        if valor > self.pontos:
            self.pontos = 0
        else:
            self.pontos -= valor
    
    def ganhar_pontos (self, valor):
        self.pontos += valor
          