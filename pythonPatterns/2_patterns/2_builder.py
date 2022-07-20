# Builder Pattern
# --------------------------------
# - Some objects are simple and can be created in a single initializer call
# - Other objects require a lot of ceremony to create
# - Having an object with 10 initializer arguments is not productive
# - Instead, opt for piecewise construction
# --------------------------------
# - Builder provides an API for constructing an object step-by-step

# Formal definition:
# - When piecewise object construction is complicated,
#   provide an API for doing it succintly

text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))


# Too much lines and a lot of details in tag
# --------------------------------
words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f"  <li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))

# How to enforce the construction of the tags and details


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.text = text
        self.name = name
        self.elements = []

    def _str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e._str(indent + 1))
        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self._str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def __str__(self):
        return str(self.__root)


builder = HtmlBuilder("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print("Ordinary Builder:")
print(builder)
