from Pessoa import pessoa

class Eleitor(pessoa):
        def __init__(self, nome, cpf):
            pessoa.__init__(self, nome, cpf)
            self.voto = 0
        def setVoted(self):
            self.voto = 1
        def getVoted(self):
            return self.voto
