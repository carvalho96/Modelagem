from Pessoa import pessoa

class Eleitor(pessoa):
        def __init__(self, nome, cpf):
            super(Candidato , self).__init__(nome, cpf)
            voto = 0
        def setVoted():
            voto = 1
        def getVoted():
            return voto
