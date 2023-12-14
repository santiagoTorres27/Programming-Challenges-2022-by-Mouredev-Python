from enum import Enum


class Kind(Enum):
    WATER = 1,
    FIRE = 2,
    PLANT = 3,
    ELECTRIC = 4


class Pokemon:
    def __init__(self, name: str, attack: int, defense: int, kind: Kind):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.kind = kind
        self._life = 500

        if self.kind == Kind.WATER:
            self.effectiveness = 2
        elif self.kind == Kind.FIRE:
            self.effectiveness = 1
        elif self.kind == Kind.PLANT:
            self.effectiveness = 0.5
        elif self.kind == Kind.ELECTRIC:
            self.effectiveness = 2

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = value

    def hit(self):
        # daño = 50 * (ataque / defensa) * efectividad
        return 50 * (self.attack // self.defense) * self.effectiveness

    def receive_damage(self, damage):
        self.life = self.life - damage

    def __str__(self):
        return f"{self.name} | Attack: {self.attack} | Defense: {self.defense} | Effectiveness: {self.effectiveness}"
