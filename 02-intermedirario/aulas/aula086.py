# yield from

def generator_1():
    print('início_1')
    yield 0
    yield 1
    yield 2
    print('fim_1')

def generator_3():
    print('início_3')
    yield 10
    yield 20
    yield 30
    print('fim_3')

def generator_2(gen=None):
    print('início_2')
    if gen is not None:
        yield from gen
    yield 3
    yield 4
    yield 5
    print('fim_2')

gen_1 = generator_2(generator_1())
gen_2 = generator_2(generator_3())
gen_3 = generator_2()

for num in gen_1:
    print(num)
print()
for num in gen_2:
    print(num)
print()
for num in gen_3:
    print(num)
print()