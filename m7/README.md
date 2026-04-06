```mermaid
classDiagram

class Creature {
    <<abstract>>
    +name
    +type_creature
    +attack()
    +describe()
}

Creature <|-- Flameling
Creature <|-- Pyrodon
Creature <|-- Aquabub
Creature <|-- Torragon

class Flameling {
    <<concrete>>
}

class Pyrodon {
    <<concrete>>
}

class Aquabub {
    <<concrete>>
}

class Torragon {
    <<concrete>>
}

class FlameFactory {
    +createFlameling()
    +createPyrodon()
}

class AquaFactory {
    +createAquabub()
    +createTorragon()
}

FlameFactory --> Flameling
FlameFactory --> Pyrodon
AquaFactory --> Aquabub
AquaFactory --> Torragon