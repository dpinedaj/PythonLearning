import unittest


class Game:
    def __init__(self):
        self.creatures = []


class Creature:
    def __init__(self, game, attack, defense):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        return self.initial_attack + len(
            [i for i in self.game if isinstance(i, GoblinKing)]
        )

    @property
    def defense(self):
        return self.initial_defense + len(
            [i for i in self.game if isinstance(i, Goblin)]
        )

    def __str__(self):
        return f"{self.attack} / {self.defense}"


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)


class FirstTestSuite(unittest.TestCase):
    def test_1_goblin(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

    def test_2_goblin(self):
        game = Game()

        goblin1 = Goblin(game)
        goblin2 = Goblin(game)

        game.creatures.append(goblin1)
        game.creatures.append(goblin2)

        self.assertEqual(1, goblin1.attack)
        self.assertEqual(2, goblin1.defense)

    def test_1_goblin_1_king(self):
        game = Game()

        goblin1 = Goblin(game)
        goblin2 = GoblinKing(game)

        game.creatures.append(goblin1)
        game.creatures.append(goblin2)

        self.assertEqual(2, goblin1.attack)
        self.assertEqual(2, goblin1.defense)
