@startuml plt12
class Motore {
    - numero_seriale: string
    - tipo: string
    - auto: Auto
    
    + get_numero_seriale(): string
    + set_numero_seriale(numero_seriale: string): void
    + get_tipo(): string
    + set_tipo(tipo: string): void
    + collega_auto(auto: Auto): void
}
class Auto {
    - marca: string
    - modello: string
    - motore: Motore
    
    + get_marca(): string
    + set_marca(marca: string): void
    + get_modello(): string
    + set_modello(modello: string): void
    + collega_motore(motore: Motore): void
    + verifica_associazione(): string
}
Motore "1" -- "1" Auto : associazione uno a uno

@enduml