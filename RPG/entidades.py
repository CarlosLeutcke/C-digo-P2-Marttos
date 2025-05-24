class Jogador:
    def __init__(self, nome, nivel, classe, npc=False):
        self.nome = nome              # armazena o nome do jogador
        self.nivel = nivel            # armazena o nível do jogador (1–20)
        self.classe = classe          # armazena a classe escolhida (Guerreiro, Mago, etc.)
        self.npc = npc                # flag que indica se é um NPC (True) ou jogador humano
        self.hp = 100                 # inicializa pontos de vida em 100
        self.defendeu = False         # flag para marcar se usou defesa no turno anterior

    def __repr__(self):
        prefixo = "[NPC] " if self.npc else ""  # prefixa “[NPC] ” se for um NPC
        return f"{prefixo}{self.nome} (Nível {self.nivel} - {self.classe} | HP: {self.hp})"# retorna representação legível com nome, nível, classe e HP

class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome              # armazena o nome do time
        self.jogadores = tuple(jogadores)  # converte lista de jogadores em tupla (imutável)

    def __repr__(self):
        return self.nome             # representação do time é simplesmente seu nome

    def detalhes(self):
        linhas = [self.nome]         # inicia lista de linhas com o nome do time
        for j in self.jogadores:     # itera por cada jogador na tupla
            linhas.append(str(j))    # adiciona a string de cada jogador
        return "\n".join(linhas)     # retorna texto com quebras de linha entre cada item
