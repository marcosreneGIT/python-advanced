from dataclasses import dataclass, field, fields


@dataclass(frozen=True) # não permite alterar os valores já definidos
class Homen:
    nome: str
    idade: int
    sexo: str = 'M'
    endereco: list[str] = field(default_factory=list) 
    # maneira correta de se pré definir uma lista (ou qualquer objeto mutável).                                                    
                                                      
if __name__ == '__main__':
    homen_0 = Homen('Marcos', 21)
    
    print(homen_0)
    print(fields(homen_0))