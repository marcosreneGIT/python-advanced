from contextlib import contextmanager

@contextmanager
def my_open(path_file, mode):
    try:
        print('Open file.')
        file = open(path_file, mode, encoding='utf8')

        yield file
        
    finally:
        print('Close file.')
        file.close()

with my_open('aula143.txt', 'w') as file:
    file.write('...')
    
    print('with', file)