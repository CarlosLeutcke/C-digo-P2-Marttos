class No:
    def __init__(self, dado):
        self.dado = dado           # armazena o valor (dado) no nó
        self.proximo = None        # referência para o próximo nó (inicialmente vazio)

class FilaEncadeada:
    def __init__(self):
        self.inicio = None         # aponta para o primeiro nó da fila
        self.fim = None            # aponta para o último nó da fila

    def enfileirar(self, item):
        novo = No(item)            # cria um novo nó com o item
        if not self.fim:           # se a fila estiver vazia
            self.inicio = self.fim = novo  # início e fim passam a ser o novo nó
        else:
            self.fim.proximo = novo  # liga o antigo fim ao novo nó
            self.fim = novo          # atualiza o fim para o novo nó

    def desenfileirar(self):
        if not self.inicio:        # se a fila estiver vazia
            return None            # nada a desenfileirar
        item = self.inicio.dado    # pega o dado do nó do início
        self.inicio = self.inicio.proximo  # avança o início para o próximo nó
        if not self.inicio:        # se agora não houver mais nós
            self.fim = None        # limpa também a referência ao fim
        return item                # retorna o dado removido

    def vazia(self):
        return self.inicio is None # retorna True se não houver nenhum nó na fila
