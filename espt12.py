class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None

    def get_numero_seriale(self):
        return self.numero_seriale

    def set_numero_seriale(self, numero_seriale):
        self.numero_seriale = numero_seriale

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def collega_auto(self, auto):
        if self.auto is not None:
            print("Questo motore è già associato a un'auto.")
        else:
            self.auto = auto
            auto.collega_motore(self)

class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.motore = None

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    def collega_motore(self, motore):
        if self.motore is not None:
            print("Questa auto è già associata a un motore.")
        else:
            self.motore = motore

    def verifica_associazione(self):
        if self.motore is not None and self.motore.auto is self:
            return f"L'auto {self.marca} {self.modello} è associata al motore {self.motore.numero_seriale} ({self.motore.tipo})."
        else:
            return "L'auto non è associata correttamente a un motore."