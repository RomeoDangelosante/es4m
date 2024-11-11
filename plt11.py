@startuml PLT11 
class Ricetta {
    - nome: string
    - tempo_preparazione: int
    - ingredienti: List<string>
    - difficolta: string
    
    + get_nome(): string
    + set_nome(nome: string): void
    + get_tempo_preparazione(): int
    + set_tempo_preparazione(tempo: int): void
    + get_ingredienti(): List<string>
    + set_ingredienti(ingredienti: List<string>): void
    + get_difficolta(): string
    + set_difficolta(difficolta: string): void
    + aggiungi_ingrediente(ingrediente: string): void
    + calcola_tempo_totale(ricette: List<Ricetta>): int
}

class Primo {
    - tipo_pasta: string
    - sugo: string
    
    + get_tipo_pasta(): string
    + set_tipo_pasta(tipo_pasta: string): void
    + get_sugo(): string
    + set_sugo(sugo: string): void
}

class Secondo {
    - tipo_carne: string
    - cottura: string
    
    + get_tipo_carne(): string
    + set_tipo_carne(tipo_carne: string): void
    + get_cottura(): string
    + set_cottura(cottura: string): void
}

class Dolce {
    - zucchero: string
    - tipo_dolce: string
    
    + get_zucchero(): string
    + set_zucchero(zucchero: string): void
    + get_tipo_dolce(): string
    + set_tipo_dolce(tipo_dolce: string): void
}

Ricetta <|-- Primo
Ricetta <|-- Secondo
Ricetta <|-- Dolce

class VerificaIngredienti {
    + verifica_ingredienti(ricette: List<Ricetta>, ingredienti_disponibili: List<string>): List<Ricetta>
}

class StampaRicette {
    + stampa_ricette(ricette: List<Ricetta>): void
}

@enduml