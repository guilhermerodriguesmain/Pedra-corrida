import os
from Classes.mesa import Mesa
from Classes.player import Jogador
from Classes.pedra_rolada import JogoPedraRolada

# instanciando objetos
jogador = Jogador('',0)
mesa = Mesa(0)
jogo = JogoPedraRolada(jogador, mesa)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_jogo():
    nome = input("Digite seu nome: ")
    pontos_iniciais = int(input("Digite a quantidade de pontos iniciais: "))
    jogador.nome = nome
    jogador.pontos = pontos_iniciais
    mesa.pontos = pontos_iniciais
    
def mostrar_regras():
    print("""
====== BEM-VINDO AO JOGO PEDRA ROLADA ======

REGRAS DO JOGO:

→ Cada jogador começa com uma quantidade igual de pontos (que representam as pedrinhas em mãos).
→ Em cada rodada, os jogadores escolhem:
    - Um palpite para o total de pontos revelados na rodada.
    - Quantos pontos (entre 1 e 6) desejam revelar de sua pontuação total.
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

    
mostrar_regras()

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
    print("      ====== Jogo Pedra Rolada ======\n\n")
    print(f"{jogador.nome}: {jogador.pontos} Pontos   ||   Mesa: {mesa.pontos} Pontos \n")
    print(f"seu palpite: {jogador.palpite}   -  palpite mesa: {mesa.reveladas}")
    
    
    # se usuario perder
    if jogador.pontos <= 0:
        print("Você não tem mais pontos. Fim de jogo!")
        nova_partida = input("Deseja jogar uma nova partida? (s/n): ").lower()
        if nova_partida == 's':
            jogo.jogar_rodada()
        elif nova_partida == 'n':
            print("Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida. Encerrando o jogo.")
            break
    
    # se usuario ganhar
    if jogador.pontos <= 0:
        print("Você não tem mais pontos. Fim de jogo!")
        nova_partida = input("Deseja jogar uma nova partida? (s/n): ").lower()
        if nova_partida == 's':
            jogo.jogar_rodada()
        elif nova_partida == 'n':
            print("Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida. Encerrando o jogo.")
            break
    
    jogo.jogar_rodada()
    

    