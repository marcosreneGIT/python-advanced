# modularização - entendendo os seus próprios módulos Python

# o primeiro módulo executado chama-se __main__
print('Este módulo se chama', __name__)

# você pode importar outro módulo inteiro ou parte do módulo
import python_intermedirario.aulas.aula092.modulo092 as modulo092

# o python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# ele não reconhece pastas e módulos acima do __main__ por padrão
# o python conhece todos os módulos e pacotes presentes nos caminhos de sys.path


