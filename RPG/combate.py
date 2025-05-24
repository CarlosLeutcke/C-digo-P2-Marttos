import random                                   # importa módulo para geração de números aleatórios
from entidades import Time                       # importa classe Time para tipagem e acesso a jogadores

frases_ataque = {                                # dicionário de frases por tipo de ação
    'ataque leve': [
        "Sinta a minha lâmina leve!",
        "Um golpe rápido para você!",
        "Não pisque, ou vai perder!",
        "Ataque leve, mas certeiro!",
        "Velocidade é meu aliado!",
        "Um toque suave, porém letal!"
    ],
    'ataque médio': [
        "Agora vai um golpe na medida!",
        "Ataque médio em ação!",
        "Pressão moderada!",
        "Sinta a força desse golpe!",
        "Um ataque no ponto certo!",
        "Certeiro e potente!"
    ],
    'ataque pesado': [
        "Esse é o meu golpe mais forte!",
        "Prepare-se para o devastador!",
        "Ataque pesado! Não escape!",
        "Vou esmagar você agora!",
        "Força total neste golpe!",
        "Sinta o poder bruto!"
    ],
    'defesa': [
        "Bloqueio perfeito!",
        "Desviei habilmente!",
        "Minha defesa não falha!",
        "Protegido contra o golpe!",
        "Nenhum dano passou!",
        "Contra-ataque pronto!"
    ]
}

def simular_luta(t1: Time, t2: Time) -> Time:
    # Inicialização de estados
    for p in t1.jogadores + t2.jogadores:        # para cada jogador de ambos os times
        p.hp = 100                               # define HP inicial como 100
        p.defendeu = False                       # reseta flag de defesa

    # Iniciativas
    ordem = []                                   # lista para guardar tuplas (iniciativa, jogador)
    print("Iniciativas:")                        # imprime cabeçalho
    for p in t1.jogadores + t2.jogadores:        # calcula iniciativa para cada jogador
        ini = random.randint(1,20)               # rola d20 aleatório
        ordem.append((ini, p))                   # armazena valor e referência
        print(f"{p.nome}: {ini}")                # exibe iniciativa
    ordem.sort(key=lambda x: x[0], reverse=True) # ordena tuplas da maior para a menor
    ordem = [p for _, p in ordem]                # extrai apenas jogadores na ordem
    print("Ordem de ação:", ", ".join(p.nome for p in ordem))  # exibe sequência de ação

    round_num = 1                                 # contador de rodada
    while any(p.hp > 0 for p in t1.jogadores) and any(p.hp > 0 for p in t2.jogadores): # enquanto ambos os times tiverem jogadores com HP > 0
        print(f"\n--- Round {round_num} ---")    # cabeçalho de round
        for p in ordem:                          # itera conforme a ordem de iniciativa
            if p.hp <= 0:                        # pula quem estiver morto
                continue
            adversarios = t2.jogadores if p in t1.jogadores else t1.jogadores  # escolhe time adversário
            vivos = [a for a in adversarios if a.hp > 0]  # filtra adversários vivos
            if not vivos:                        # se não houver mais vivos, interrompe loop
                break

            # Escolha de ação
            if p.npc:
                acao = random.choice(list(frases_ataque.keys()))  # NPC escolhe ação aleatória
            else:
                print(f"\nVez de {p.nome} (HP {p.hp}). Escolha ação:")  # prompt para jogador humano
                ops = ['ataque leve', 'ataque médio', 'ataque pesado', 'defesa']
                for i, op in enumerate(ops, 1):  # exibe opções numeradas
                    print(f"{i}. {op.title()}")
                acao = ops[int(input("Opção: ").strip()) - 1]  # captura escolha do usuário

            # Definir alvo ou defesa
            alvo = None                            # inicializa variável alvo
            if acao != 'defesa':                   # se for ataque
                if p.npc:
                    alvo = random.choice(vivos)    # NPC escolhe alvo aleatório
                else:
                    print("Escolha alvo:")        # prompt para jogador escolher alvo
                    for i, a in enumerate(vivos, 1):
                        print(f"{i}. {a.nome} (HP {a.hp})")
                    alvo = vivos[int(input("Opção: ").strip()) - 1]  # escolhe o alvo
                print(f"{p.nome} escolheu {acao} em {alvo.nome}.")
            else:
                p.defendeu = True                  # marca que jogador se defendeu
                print(f"{p.nome} escolheu defesa.")

            # Frase de combate
            frase = random.choice(frases_ataque[acao])  # escolhe frase aleatória
            print(f"{p.nome} diz: {frase}")        # exibe frase

            # Cálculo de dano
            if acao.startswith('ataque'):           # se ação for ataque
                base = {'ataque leve': 10, 
                        'ataque médio': 18, 
                        'ataque pesado': 30}[acao]  # define dano base
                bloqueio = 20 if alvo.defendeu else 0  # dano bloqueado se alvo defendeu
                dano = max(base - bloqueio, 0)     # garante dano não negativo
                alvo.hp -= dano                     # aplica dano ao HP do alvo
                print(f"{alvo.nome} recebe {dano} de dano. HP agora: {max(alvo.hp, 0)}") 
                alvo.defendeu = False               # reseta flag de defesa do alvo
                if alvo.hp <= 0:
                    print(f"{alvo.nome} foi derrotado por {p.nome}!")  # exibe mensagem de derrota

            if not any(a.hp > 0 for a in adversarios):  # se todos adversários estão mortos
                break                              # encerra loop de turnos
        round_num += 1                            # incrementa contador de rodada

    vencedor = t1 if any(p.hp > 0 for p in t1.jogadores) else t2  # determina o time vencedor
    print(f"\nVencedor da luta: {vencedor.nome}")  # exibe o nome do vencedor
    return vencedor                             # retorna o time vencedor
