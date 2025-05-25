import random                                    # importa módulo para operações aleatórias
from estrutura import FilaEncadeada               
from entidades import Jogador                     

# listas e estruturas globais
jogadores = []                                   # lista para armazenar todos os jogadores (NPCs e humanos)
nomes_registrados = set()                        # set para garantir nomes únicos
fila_jogadores = FilaEncadeada()                 # fila para controlar ordem de cadastro
times = {}                                       # dicionário para armazenar times posteriormente

# constantes de dados
NOMES_NPC = ["João", "Maria", "Fulano", "Cleber", "Bianca", 
             "Arthur", "Iago", "Igor", "Fernado", "Julia"]  
CLASSES = ["Guerreiro", "Mago", "Clérigo", "Ladino"]       

def gerar_npcs(quantidade):
    """Gera 'quantidade' de NPCs com nomes, níveis e classes aleatórias."""
    for _ in range(quantidade):                 # repete até gerar todos os NPCs
        while True:
            nome = random.choice(NOMES_NPC) + str(random.randint(1,99)) # escolhe nome aleatório + número para evitar duplicatas
            if nome not in nomes_registrados:    # verifica unicidade de nome
                break                            # sai do loop quando nome é único
        nivel = random.randint(1,20)             # sorteia nível entre 1 e 20
        classe = random.choice(CLASSES)          # seleciona classe aleatória
        npc = Jogador(nome, nivel, classe, npc=True)  # cria instância de Jogador marcada como NPC
        jogadores.append(npc)                    # adiciona NPC à lista de jogadores
        nomes_registrados.add(nome)              # registra o nome no set de nomes usados
        fila_jogadores.enfileirar(npc)           # enfileira o NPC na fila encadeada
    print(f"Gerados {quantidade} NPCs e adicionados à fila.")  

def registrar_jogador():
    """Solicita dados do usuário para cadastrar um novo jogador humano."""
    nome = input("Digite o nome do jogador: ").strip()  # lê e limpa espaços do nome
    if nome in nomes_registrados:                # verifica se já existe um jogador com esse nome
        print("Jogador já registrado.")          # avisa duplicata
        return                                   # aborta cadastro

    while True: # loop para validar nível
        nivel_in = input("Digite o nível (1-20 ou R para randômico): ").strip().upper()
        if nivel_in == 'R':
            nivel = random.randint(1,20)         # escolhe nível aleatório
            print(f"Nível randômico selecionado: {nivel}")
            break
        if nivel_in.isdigit() and 1 <= int(nivel_in) <= 20:
            nivel = int(nivel_in)                # converte entrada válida em inteiro
            break
        print("Entrada inválida. Informe um número entre 1 e 20 ou 'R'.")

    while True: # loop para escolher classe
        print("Escolha a classe:")
        for i, cl in enumerate(CLASSES, 1):      # exibe opções numeradas de classes
            print(f"{i}. {cl}")
        esc = input("Opção: ").strip()
        if esc.isdigit() and 1 <= int(esc) <= len(CLASSES):
            classe = CLASSES[int(esc)-1]         # seleciona classe com base na escolha
            break
        print("Opção inválida.")

    jogador = Jogador(nome, nivel, classe)      # cria instância de Jogador humano
    jogadores.append(jogador)                   # adiciona jogador à lista
    nomes_registrados.add(nome)                  # registra nome no set
    fila_jogadores.enfileirar(jogador)           # enfileira o jogador na fila
    print(f"Registrado {jogador} e adicionado à fila.")  # feedback ao usuário
