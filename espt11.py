class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tempo_preparazione(self):
        return self.tempo_preparazione

    def set_tempo_preparazione(self, tempo):
        self.tempo_preparazione = tempo

    def get_ingredienti(self):
        return self.ingredienti

    def set_ingredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def get_difficolta(self):
        return self.difficolta

    def set_difficolta(self, difficolta):
        self.difficolta = difficolta

    def aggiungi_ingrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)

    @staticmethod
    def calcola_tempo_totale(ricette):
        tempo_totale = sum(ricetta.get_tempo_preparazione() for ricetta in ricette)
        return tempo_totale

class Primo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

class Secondo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura

class Dolce(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, zucchero, tipo_dolce):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.zucchero = zucchero
        self.tipo_dolce = tipo_dolce

    def get_zucchero(self):
        return self.zucchero

    def set_zucchero(self, zucchero):
        self.zucchero = zucchero

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def set_tipo_dolce(self, tipo_dolce):
        self.tipo_dolce = tipo_dolce

def verifica_ingredienti(ricette, ingredienti_disponibili):
    ricette_possibili = []
    for ricetta in ricette:
        if all(ingrediente in ingredienti_disponibili for ingrediente in ricetta.get_ingredienti()):
            ricette_possibili.append(ricetta)
    return ricette_possibili

def stampa_ricette(ricette):
    for ricetta in ricette:
        print(f"Nome: {ricetta.get_nome()}")
        print(f"Tempo di preparazione: {ricetta.get_tempo_preparazione()} minuti")
        print(f"Difficoltà: {ricetta.get_difficolta()}")
        print(f"Ingredienti: {', '.join(ricetta.get_ingredienti())}")
        if isinstance(ricetta, Primo):
            print(f"Tipo di pasta: {ricetta.get_tipo_pasta()}")
            print(f"Sugo: {ricetta.get_sugo()}")
        elif isinstance(ricetta, Secondo):  
            print(f"Tipo di carne: {ricetta.get_tipo_carne()}")
            print(f"Cottura: {ricetta.get_cottura()}")
        elif isinstance(ricetta, Dolce):
            print(f"Zucchero: {ricetta.get_zucchero()}")
            print(f"Tipo di dolce: {ricetta.get_tipo_dolce()}")
        print("="*40)