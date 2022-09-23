# Overview

# Motivation:
# Unethical behavior by an employee; who takes the blame
# - Employee
# - Manager
# - CEO
# You click a graphical element on a form
# - Button handles it, stops further processing
# - Underlying group box
# - Underlying window
# CCG computer game
# - Creature has attack and defense values
# - Those can be buoosted by other properties

# A chain of components who all get a change to proceess a command or a query,
# optionally having default processing implementation and
# ability to terminate the processing chain.

from enum import Enum
from abc import ABC


class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s atatck")
        self.creature.attack *= 2
        super().handle()


# if __name__ == "__main__":
#     goblin = Creature("goblin", 1, 1)
#     print(goblin)

#     root = CreatureModifier(goblin)
#     root.add_modifier(DoubleAttackModifier(goblin))

#     root.handle()
#     print(goblin)


# Concepts
# Command: asking for an action or change (e.g, please set your attack value to 2)
# Query: asking for information (e.g, plesae give me your attack value)
# CQS: having separate means of sending commands and queries to e.g., direct field access


# Broker chain
# event broker (observer)
# CQS


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        # query
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack} / {self.defense})"


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)

    print(goblin)
