class Gato:
    '''Classe para trabalhar com gatos'''
    tipo_animal = 'Felino'
    def __init__(self, nome):
        '''Inicializa o objeto capturando o nome do animal'''
        self.nome = nome
        print('Seu gatinho se chama', self.nome)
    
    def peso_gato(self, peso):
        self.peso = peso
        if (self.peso >= 5.0):
            print('Seu gato está gordinho')
        elif (self.peso >= 3.0):
             print('Seu gato está no peso normal')
        else:
             print('Seu gato está abaixo do peso')

    def _dieta_especial_gato(self):
        self.msg = 'Tudo ok'
        if self.peso >= 5.0:
            print('Diminua a ração do gatinho')
        elif self.peso < 3.0:
            print('Aumente a ração do gatinho')
        return self.msg

    def _dados_do_gato(self):
        print('\nO gato',self.nome, 'possui', self.peso, 'kg')
        print(self._dieta_especial_gato())

nome_gato = input('Insira o nome do seu gato')
g1 = Gato(nome_gato)

peso = float(input('\n Qual o peso do seu gato em kg?:  '))
g1.peso_gato(peso)

g1._dados_do_gato()