import sys                                   
import random                                
from create import jogadores, times, gerar_npcs, registrar_jogador  
from entidades import Jogador, Time          
from combate import simular_luta             
from torneio import simular_torneio, mostrar_colocacoes 

def listar_jogadores():
    if not jogadores:                         # verifica se a lista de jogadores está vazia
        print("Nenhum jogador cadastrado.")   # avisa que não há jogadores registrados
    else:
        print("\nJogadores registrados:")     # exibe cabeçalho da listagem
        for j in jogadores:                   # itera sobre cada objeto Jogador
            print(j)                          # imprime a representação de cada jogador

def criar_times():
    if len(jogadores) < 2:                    # exige ao menos 2 jogadores para formar times
        print("É necessário pelo menos 2 jogadores para formar times.")
        return                                # sai da função se não houver jogadores suficientes

    try:
        tamanho = int(input("Digite o tamanho de cada time (mínimo 2): ").strip())# solicita ao usuário o tamanho de cada time
        if tamanho < 2:                       # valida se o tamanho é pelo menos 2
            print("O tamanho mínimo do time deve ser 2.")
            return
    except ValueError:                         # trata entradas não numéricas
        print("Valor inválido. Digite um número inteiro.")
        return

    if len(jogadores) % tamanho != 0:         # verifica se o total de jogadores é divisível pelo tamanho
        print("O número de jogadores não é divisível pelo tamanho do time.")
        return

    opc = input("Deseja nomear times pelo NPC de maior nível? (s/n): ").strip().lower()# pergunta se quer usar o NPC de maior nível para nomeação
    usar_npc = (opc == 's')                   # define flag para uso de NPC na criação de nome
    random.shuffle(jogadores)                 # embaralha ordem dos jogadores antes de agrupar
    times.clear()                             # limpa dicionário de times anterior
    manual = {}                               # dicionário para marcar nomes definidos manualmente

    for i in range(0, len(jogadores), tamanho):  # percorre em saltos do tamanho do time
        grupo = jogadores[i:i+tamanho]        # seleciona sublista de jogadores para este time
        if usar_npc:
            maior = max(grupo, key=lambda p: p.nivel)  # identifica NPC de maior nível no grupo
            ordenado = [maior] + [p for p in grupo if p is not maior]  # coloca o maior na frente e depois o restante
            default_name = f"Time_{i//tamanho+1}_{maior.nome}{maior.nivel}"# monta nome padrão baseado no NPC
        else:
            ordenado = grupo
            default_name = f"Time_{i//tamanho+1}"  # nome padrão sem uso de NPC

        escolha_nome = input(
            f"Deseja definir um nome personalizado para o time {i//tamanho+1}? (s/n): "
        ).strip().lower()                      # pergunta se deseja nomear manualmente
        if escolha_nome == 's':
            nome_time = input("Digite o nome do time: ").strip()  # recebe nome manual
            if not nome_time:
                nome_time = default_name      # usa padrão se entrada ficar vazia
            manual[nome_time] = True          # marca como nome manual
            print(f"TIME NOMEADO MANUALMENTE: {nome_time}")
        else:
            nome_time = default_name
            manual[nome_time] = False         # marca como nome automático
            print(f"TIME NOMEADO AUTOMATICAMENTE: {nome_time}")

        times[nome_time] = Time(nome_time, ordenado)  # cria e armazena o time no dicionário

    print("\nTimes criados:")                 # mostra todos os times criados
    for t in times.values():
        print(t.detalhes())                   # imprime detalhes de cada time
        print()                               

def listar_times():
    if not times:                             # verifica se há times criados
        print("Nenhum time criado.")          # avisa se não houver
    else:
        print("\nTimes:")                     # cabeçalho da listagem de times
        for t in times.values():              # percorre todos os objetos Time
            print(t.detalhes())               # imprime detalhes de cada time
            print()                          

def menu_principal():
    print("GAME ON!")                        
    opcoes = [4, 8, 16]                       
    while True:
        print("\nEscolha o número de participantes do torneio:")
        for i, val in enumerate(opcoes, 1):   # exibe cada opção numerada
            print(f"{i}. {val} jogadores")
        escolha = input("Opção: ").strip()    # lê escolha do usuário
        if escolha in {'1', '2', '3'}:
            total = opcoes[int(escolha) - 1] # converte escolha em número de participantes
            break                            # sai do loop após escolha válida
        else:
            print("Opção inválida. Tente novamente.")

    while len(jogadores) < total:            # enquanto não atingir total de jogadores
        falta = total - len(jogadores)       
        print(f"Faltam {falta} jogadores.")
        print("1. Registrar manual")
        print("2. Gerar NPCs")
        e = input("Opção: ").strip()         # lê método de cadastro
        if e == '1':
            registrar_jogador()              # chama função de registro manual
        elif e == '2':
            gerar_npcs(falta)                # gera número restante de NPCs

    while True:                               
        print("\n=== Menu ===")
        print("1. Listar jogadores")
        print("2. Criar times")
        print("3. Listar times")
        print("4. Simular torneio")
        print("5. Sair")
        c = input("Opção: ").strip()          
        if c == '1':
            listar_jogadores()                
        elif c == '2':
            criar_times()                     
        elif c == '3':
            listar_times()                    
        elif c == '4':
            # simula torneio e, se houver campeão, mostra colocações
            campeao, eliminacoes, total_fases = simular_torneio(times)
            if campeao:
                mostrar_colocacoes(campeao, eliminacoes, total_fases)
        elif c == '5':
            print("Game OFF!")                
            sys.exit(0)                       # encerra o programa
        else:
            print("Opção inválida. Tente novamente.") 

if __name__ == '__main__':
    menu_principal()                        # inicia execução chamando o menu principal
