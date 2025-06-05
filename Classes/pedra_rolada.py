
class JogoPedraRolada:
    def __init__(self, jogador, mesa):
        self.jogador = jogador
        self.mesa = mesa
        
    def jogar_rodada(self):
        self.jogador.fazer_palpite()
        self.jogador.revelar_pedras()
        self.mesa.revelar_pedras()
        soma_total = self.jogador.reveladas + self.mesa.reveladas
        diferenca = abs(self.jogador.palpite - soma_total)

        if diferenca == 0:
            self.jogador.ganhar_pontos(3)
            self.mesa.perder_pontos(3)
        elif diferenca <= 2:
            self.jogador.ganhar_pontos(2)
            self.mesa.perder_pontos(2)
        elif diferenca == 3:
            self.jogador.ganhar_pontos(1)
            self.mesa.perder_pontos(1)
        else:
            self.jogador.perder_pontos(2)
            self.mesa.ganhar_pontos(2)

        print(f"Seu Palpite: {self.jogador.palpite}")
        print(f"Soma total: {soma_total}")
        print(f"Pontos transferidos: {diferenca}")

        print(f"{self.jogador.nome}:")
        self.jogador.mostrar_estado()
        print("Mesa:")
        self.mesa.mostrar_estado()
        