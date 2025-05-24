import random                                    # importa módulo para gerar números aleatórios
from combate import simular_luta                  # importa função de simulação de luta entre dois times

def simular_torneio(times: dict):
    """
    Executa o torneio em eliminação direta e registra em que fase cada time foi eliminado.
    Retorna:
      - campeao: o objeto Time vencedor (1º lugar)
      - eliminacoes: dicionário {time: fase_em_que_foi_eliminado}
      - total_fases: número total de fases realizadas
    """
    if not times:                                 # se o dicionário de times estiver vazio
        print("Crie times primeiro.")             # avisa o usuário para criar times
        return None, {}, 0                       # retorna valores padrão (nenhum campeão)

    fila = list(times.values())                   # converte os objetos Time em uma lista
    random.shuffle(fila)                          # embaralha a lista para confrontos aleatórios

    fase = 1                                      # inicializa contador de fases
    eliminacoes = {}                              # dicionário para mapear time eliminado → fase
    while len(fila) > 1:                          # enquanto houver mais de um time na fila
        print(f"\n== Fase {fase} {fila[0]} contra {fila[1]} ==")  # exibe primeiro confronto da fase
        vencedores = []                           # lista temporária para vencedores desta fase
        for i in range(0, len(fila), 2):          # percorre a lista de dois em dois
            t1, t2 = fila[i], fila[i+1]           # seleciona par de times adjacentes
            vencedor = simular_luta(t1, t2)       # chama função que retorna o time vencedor
            perdedor = t1 if vencedor is t2 else t2  # determina qual time perdeu
            eliminacoes[perdedor] = fase         # registra a fase em que o perdedor caiu
            vencedores.append(vencedor)           # adiciona vencedor à lista de vencedores
        fila = vencedores                         # substitui fila original pela dos vencedores
        fase += 1                                 # incrementa contador de fases

    campeao = fila[0]                             # último time restante é o campeão
    total_fases = fase - 1                        # calcula total de fases do torneio
    print(f"\nCampeão: {campeao.nome}!")          # exibe nome do campeão
    return campeao, eliminacoes, total_fases     # retorna campeão, mapa de eliminações e total de fases

def mostrar_colocacoes(campeao, eliminacoes: dict, total_fases: int):
    """
    Exibe a colocação final de todos os times em ordem:
      1º lugar — campeão
      2º lugar em diante — conforme fase de eliminação, do mais avançado ao inicial
    """
    ranking = [campeao.nome]                      # inicia lista de ranking com o campeão em 1º
    print("\n--- Colocação Final ---")             # imprime título da seção de colocações
    print(f"1º Lugar: {campeao.nome}")            # exibe o campeão como 1º lugar

    eliminacoes.pop(campeao, None)                # remove o campeão do dicionário de eliminações

    # agrupa os times restantes por fase de eliminação
    fases_por_time = {}                           
    for time, fase in eliminacoes.items():        # itera sobre cada par (time, fase)
        fases_por_time.setdefault(fase, []).append(time)# cria ou adiciona time à lista da sua fase

    # ordena as fases de forma decrescente (fase maior = chegada mais avançada)
    fases_ordenadas = sorted(
        fases_por_time.items(),                   # itens no formato (fase, [times])
        key=lambda x: x[0],                       # chave de ordenação é a própria fase
        reverse=True                              # ordena do maior para o menor
    )

    pos = 2                                       # posição atual no ranking (começa no 2º lugar)
    for fase, times_na_fase in fases_ordenadas:   # para cada fase em ordem decrescente
        for t in times_na_fase:                   # para cada time eliminado naquela fase
            sufixo = "º"                          # define sufixo ordinal (padrão "º")
            label = f"{pos}{sufixo} Lugar"        # formata string de colocação
            print(f"{label}: {t.nome}")           # exibe posição e nome do time
            ranking.append(t.nome)                # adiciona o time ao ranking final
            pos += 1                              # incrementa contador de posição

    return ranking                                 # retorna lista completa de nomes em ordem
