````markdown````

Criamos um sistema baseado em um torneio de RPG

Integrantes do Grupo
````
- Carlos Henrique Legutcke Filho — RA:1988772
- Lucas Gomes Mendonça Chagas — RA: 1996576
---
````
## 1. Requisitos
Para executar este projeto, você precisa ter instalado em sua máquina:
````
- Python 3.8+
````
---

## 2. Instalação e Configuração
1. Clonar o repositório
   ````bash
   git clone https://github.com/seu-usuario/torneio-rpg.git
   cd torneio-rpg


## 1. Estrutura de Pastas


**Torneio-RPG**
```
│
├── combate.py         # Lógica de simulação de luta entre dois times
├── create.py          # Funções de registro de jogadores e geração de NPCs
├── entidades.py       # Definição de classes Jogador e Time
├── estrutura.py       # Organização da ordem dos players e NPCs
├── main.py            # Script principal com o menu e orquestração
├── torneio.py         # Gestão do torneio e exibição das colocações
└── README.md          # Documento descritivo (este arquivo)
```

---

## 2. Visão Geral do Sistema

O sistema criado simula um torneio em grupo com combate estilo RPG, composto por:

1. **Cadastro de Jogadores**

   * Permite cadastrar um player manualmente esse player terá um nome descrito pelo usuario, um nivel podendo ser descrito pelo usuario ou randomizado e uma classe podendo ser escolhida entre 4 classes sendo eles guerreiro, mago ladino e clérigo.
   * Caso o usuário não queira criar todos os integrantes do torneio manualmente acrescentamos a funcionalidade de criar NPCs aleatórios possuindo nomes aleatórios, níveis aleatórios e uma das 4 classes aleatoriamente.
     
2. **Formação de Times**

   * Na formação de times o usuario tem que informar a quantidade de jogadores em cada time.
   * Ele podera também escolher entre nomear manualmente os times ou escolher que os nome dos times sejam dados pelo NPC ou player com maior nivel.
     
3. **Simulação de Combate**

   * O codigo possui a funcionabilidade a mais que decidimos adicionar para sabermos qual será a ordem do combate pois como é um torneio de RPG normalmente são feitos por turno,
   logo decidimos colocar uma função que calcula a iniciativa para determinar a ordem de ação.
   * Cada round ou rodada os players ou NPCs podem escolher entre usar um ataque leve/médio/pesado ou defesa que proteje contra 20 de dano.
   * Cada player ou NPC começa com 100 pontos de vida (HP) e quando o player ou NPC e derrotado o codigo nos informa por quem ele foi derrotado.
     
4. **Torneio em Eliminação Direta**

   * O codigo por padrao emparelha os times aleatoriamente como se fosse um sorteio.
   * Ele também armazena em qual fase cada time foi derrotado para mostrar a colocacao no final.
     
5. **Exibição de Colocações**

   * Quando o torneio acaba o codigo mostra quem foi o campeão (1º lugar)
   * e faz um agrupamento para os demais times conforme a fase em que foram eliminados.
     
---

## 3. Como Executar

No terminal:

```bash
python main.py
```

Siga as instruções exibidas:

* 1º Escolha o total de participantes do torneio (4, 8 ou 16).
* 2º Registrar jogadores ou gerar NPCs até completar o número.
* 3º Criar os times e nomeá-los ou nomeá-los aleatoriamente.
* 4º Simular o torneio e ver os resultados( Caso tenha criado um player o usuário escolhera qual ataque usar ou defesa e escolhera quem ele ira atacar até ele for derrotado ou ganhar o torneio).
  
---

## 4. Justificativa das Estruturas de Dados

* Ocodigo conta com Listas, Fila Encadeada, Sets, Tuplas, e Dicionário

* **Lista**

  * Armazena jogadores de forma dinâmica.
  * Permite shuffle e iteração simples.

* **Sets**

  * O set foi usado para identificar quais nomes ja foram usados para que nao oucesse 5 nomes iguais como 5 Carlos ou 5 Lucas, garantindo unicidade.
  
* **Fila Encadeada**

  * Modela a ordem de chegada dos jogadores ou NPCs.
  * Possui operações para enfileirar e desenfileirar.
    
* **Tupla**

  * Transforema a coleção de jogadores para um Time imutável após criação.
  * Ela garante que não haja alterações acidentais na composição do time.
    
* **Dicionário**

  * Mapeia nomes de times para objetos `Time.
  * Armazena, de forma direta, em qual fase cada time foi eliminado.

---
```
```
