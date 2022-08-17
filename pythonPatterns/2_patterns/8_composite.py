# -*- coding: utf-8 -*-
################################
# Composite Pattern
# Is a way to treat multiple objects and groups of objects
# with their uniform factions
# We provide an identical interface for multiple objects.
################################

# Motivation
# - Objects use other object's properties/members thorugh inheritance
# and composition
# - Composition lets us make compound objects
#   - E.g, a mathematical expression compoesd of simple expressions;
#   - or a grouping of shapes that consists of several shapes
# -  Composite design pattern is used to treat both single (scalar)
# and composite objects uniformly
#   - I.e. Foo and Sequence (yielding Foo's) have common APIs

# Definition:
# Mechanism for treating individual objects and compositions in uniform manner
from collections.abc import Iterable
from abc import ABC
import unittest


class GraphicObject:
    def __init__(self, color=None) -> None:
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self) -> str:
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    print(drawing)


# Neural Networks


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return (
            f"{self.name}, "
            f"{len(self.inputs)} inputs, "
            f"{len(self.outputs)} outputs"
        )

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    neuron1 = Neuron("n1")
    neuron2 = Neuron("n2")
    layer1 = NeuronLayer("L1", 3)
    layer2 = NeuronLayer("L2", 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)


# Exercise


class SingleValue:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list):
    def __init__(self):
        super().__init__()

    def append(self, other):
        if self == other:
            return
        if isinstance(other, int):
            super().append(other)
        else:
            for o in other:
                super().append(o)

    @property
    def sum(self):
        return sum(self)


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
