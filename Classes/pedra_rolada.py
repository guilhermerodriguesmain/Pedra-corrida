
class JogoPedraRolada:
    def __init__(self, jogador, mesa):
        self.jogador = jogador
        self.mesa = mesa
        
    def jogar_rodada(self):
        self.jogador.fazer_palpite()
        self.mesa.fazer_palpite()
        self.jogador.revelar_pedras()
        self.mesa.revelar_pedras()
        soma_total = self.jogador.reveladas + self.mesa.reveladas
        diferenca = abs(self.jogador.palpite - soma_total)
        diferenca_maquina = abs(self.mesa.palpite - soma_total)

        if diferenca == 0:# acertei o palpite
            self.jogador.ganhar_pontos(2)
            self.mesa.perder_pontos(2)
            
        elif diferenca > 0 and diferenca <= 2:# meu palpite ficou maior que zero e menor ou igual a 2

            if diferenca < diferenca_maquina: # meu palpite ficou mais próximo que o da máquina
                self.jogador.ganhar_pontos(1)
                self.mesa.perder_pontos(1)
                
            elif diferenca > diferenca_maquina:# meu palpite ficou mais distante que o da máquina
                self.jogador.perder_pontos(1)
                self.mesa.ganhar_pontos(1)
                
            else: # meu palpite ficou igual ao da máquina
                self.jogador.ganhar_pontos(0)
                self.mesa.perder_pontos(0)
            
            
        elif diferenca == 3 : # meu palpite ficou exatamente 3 pontos distante do total
            
            if diferenca_maquina == 3: # palpite da máquina também ficou exatamente 3 pontos distante do total
                self.jogador.ganhar_pontos(0)
                self.mesa.perder_pontos(0)
                
            elif diferenca_maquina < 3: # meu palpite ficou mais distante que o da máquina
                self.mesa.ganhar_pontos(1)
                self.jogador.perder_pontos(1)
                
            else: # meu palpite ficou mais próximo que o da máquina
                self.jogador.ganhar_pontos(1)
                self.mesa.perder_pontos(1)
            
            self.jogador.ganhar_pontos(1)
            self.mesa.perder_pontos(1)
            
        else:# meu palpite passou muito longe
            self.jogador.perder_pontos(2)
            self.mesa.ganhar_pontos(2)

       

    def exibir_estado_jogo(self, jogador_usuario, jogador_maquina):
    
        print("      ====== Jogo Pedra Rolada ======\n\n")
        print(f"{jogador_usuario.nome}: {jogador_usuario.pontos} pontos   ||   {jogador_maquina.nome}: {jogador_maquina.pontos} pontos\n")
        print(f"Total de pontos na mesa: {jogador_usuario.pontos + jogador_maquina.pontos}\n")
        print(f"Seu palpite: {jogador_usuario.palpite}     Palpite do adversário: {jogador_maquina.palpite}\n")
        print(f"Suas pedras reveladas: {jogador_usuario.reveladas}   Pedras reveladas do adversário: {jogador_maquina.reveladas}\n")
        print(f"Total de pedras reveladas: {jogador_usuario.reveladas + jogador_maquina.reveladas}\n")
        print("============================================\n")
    
    def mostrar_regras(self):
        print("""
====== BEM-VINDO AO JOGO PEDRA ROLADA ======

REGRAS DO JOGO:

→ Cada jogador começa com uma quantidade igual de pontos (que representam as pedrinhas em mãos).
→ Em cada rodada, os jogadores escolhem:
    - Um palpite para o total de pontos revelados na rodada.
    - Quantos pontos (entre 0 e 6) desejam revelar de sua pontuação total.
→ A soma revelada dos dois jogadores será comparada com os palpites.

→ Sistema de pontuação:
    - Se o palpite de um jogador for exato, ele ganha 2 pontos do oponente.
    - Se errar por diferença de 1, ganha ou perde 1 ponto, dependendo de quem se aproximou mais.
    - Caso contrário, perde 1 ponto para o oponente.

→ O jogo continua até que um dos jogadores fique com 0 pontos.

OBJETIVO: Tome todos os pontos da mesa e vença a partida!

Boa sorte e jogue com estratégia!
============================================
""")
