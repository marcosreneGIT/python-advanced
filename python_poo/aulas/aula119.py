class Cameras:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print(f'A {self.nome} já está filmando.')
            return
        
        self.filmando = True
        print(f'A {self.nome} começou a filmar...')
        

    def para_filmar(self):
        if not self.filmando:
            print(f'A {self.nome} não está filmando.')
            return
        
        self.filmando = False
        print(f'A {self.nome} parou de filmar.')

    
    def fotografar(self):
        if self.filmando:
            print(f'A {self.nome} não permite tirar foto enquanto grava.')
            return
        
        print(f'A {self.nome} está fotografando...')


camera_0 = Cameras('Canon')
camera_1 = Cameras('Sony')

camera_0.filmar()
camera_0.filmar()
camera_0.fotografar()
camera_0.para_filmar()
camera_0.fotografar()

camera_1.para_filmar()