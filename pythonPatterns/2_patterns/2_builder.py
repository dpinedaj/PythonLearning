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

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


builder = HtmlBuilder("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print("Ordinary Builder:")
print(builder)


# Also can be a fluent interface
builder = HtmlBuilder("ul")
builder.add_child_fluent("li", "hello")\
    .add_child_fluent("li", "world")
print("Fluent Builder:")
print(builder)


# Builder Facets:
# ----------------------------------------------------------------
# -


class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.potscode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (
            f"Address: {self.street_address}, {self.potscode}, {self.city} "
            f"Employed at {self.company_name} as a {self.position} "
            f"earning {self.annual_income}"
        )


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, potscode):
        self.person.potscode = potscode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
person = (
    pb
    .lives
    .at("123 London Road")
    .in_city("London")
    .with_postcode("SW12BC")
    .works
    .at("Fabrikam")
    .as_a("Engineer")
    .earning(123000)
    .build()
)
print(person)


# How to respect Open Close principle


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self) -> str:
        return f"{self.name} born on {self.date_of_birth} " +\
            f"works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def work_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
me = (
    pb
    .called("Dimitri")
    .work_as_a("Engineer")
    .born("1/1/1980")
    .build()
)
print(me)


# Exercise

class Code:
    def __init__(self):
        self.root_name = ""
        self.fields = ""

    def __str__(self):
        return (
            f"class {self.root_name}:"
            f"\n  def __init__(self):"
            f"{self.fields}"
        )


class CodeBuilder:
    def __init__(self, root_name):
        self.code = Code()
        self.code.root_name = root_name

    def add_field(self, type, name):
        self.code.fields += f"\n    self.{type} = {name}"
        return self

    def __str__(self):
        return str(self.code)


cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
print(cb)
