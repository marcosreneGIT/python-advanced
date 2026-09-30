# abstractmethod para qualquer método já decorado (@property e setter)

# é possível criar @property @property.setter @classmethodc @staticmethod e métodos normais como abstratos
# para isso use @abstractmethod como decorator mais interno.

# foo - bar são palavras usadas como placeholder para palavras que podem mudar na programação.

from abc import ABC, abstractmethod


class AbstractFoo(ABC): 
    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): pass


class Foo(AbstractFoo):
    def __init__(self, name):
        self._name = name

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)