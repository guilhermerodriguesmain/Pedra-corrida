import os
from Classes.mesa import Maquina
from Classes.player import Jogador
from Classes.pedra_rolada import JogoPedraRolada

# instanciando objetos
jogador = Jogador('', 0)
mesa = Maquina(0)
jogo = JogoPedraRolada(jogador, mesa)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_jogo():
    print("      ====== Jogo Pedra Rolada ======\n\n")
    nome = input("Digite seu nome: ")
    pontos_iniciais = int(input("Digite a quantidade de pontos iniciais: "))
    jogador.nome = nome
    jogador.pontos = pontos_iniciais
    mesa.pontos = pontos_iniciais


limpar_tela()
jogo.mostrar_regras()

entrar = input("Deseja entrar no jogo? (s/n): ").lower()
if entrar != 's':
    print("Jogo encerrado. Até a próxima!")
    exit()
else:
    limpar_tela()
    iniciar_jogo()
    limpar_tela()

# Loop principal do jogo
# O jogo continua até que o jogador decida sair, perca todos os pontos ou ganhe todos os pontos da mesa.
while True:
    limpar_tela()
    jogo.exibir_estado_jogo(jogador, mesa)
    jogo.jogar_rodada()
    
    # Verificar condições de vitória ou derrota
    if jogador.pontos <= 0:
        jogo.exibir_estado_jogo(jogador, mesa)
        print("Você não tem mais pontos. Fim de jogo!")
        nova_partida = input("Deseja jogar uma nova partida? (s/n): ").lower()
        if nova_partida == 's':
            jogo.jogar_rodada()
            continue
        else:
            print("Obrigado por jogar! Até a próxima!")
            break
    elif mesa.pontos <= 0:
        jogo.exibir_estado_jogo(jogador, mesa)
        print("Parabéns! Você venceu o jogo!")
        nova_partida = input("Deseja jogar uma nova partida? (s/n): ").lower()
        if nova_partida == 's':
            jogo.jogar_rodada()
            continue
        else:
            print("Obrigado por jogar! Até a próxima!")
            break
