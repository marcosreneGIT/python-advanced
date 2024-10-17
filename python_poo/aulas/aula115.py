# class - classes são moldes para criar novos objetos

# as classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

# os objetos gerados pela classe podem usar seus dados internos para relaizar várias ações.

# por convenção, usamos PascalCase para nomes de classes.

class Pessoas:
    ...

pessoa = Pessoas()
pessoa.nome = 'Marcos'
pessoa.idade = 21

print(pessoa.nome)