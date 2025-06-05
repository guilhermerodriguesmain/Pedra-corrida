from Classes.mesa import Mesa
from Classes.player import Jogador
from Classes.pedra_rolada import JogoPedraRolada

# inicio do jogo:
print("====== Jogo Pedra Rolada ======")
nome = input("Digite o nome do jogador: ")
pontos_iniciais = int(input("Digite os pontos iniciais do jogador: "))
jogador = Jogador(nome, pontos_iniciais)
mesa = Mesa(10)
jogo = JogoPedraRolada(jogador, mesa)

jogo.jogar_rodada()


# loop de jogo