import Pessoa

class Candidato(Pessoa):
        def __init__(self, nome, cpf, numero, pathPhoto, Apelido, Cargo):
            super(Candidato , self).__init__(nome, cpf)
            self.numero = numero
            self.quantVotos = 0
            self.pathPhoto = pathPhoto
            self.apelido = Apelido
            self.cargo = Cargo

        def setNumero(numero):
            self.numero = numero

        def getNumero():
            return self.numero

        def setpathImg(path):
            self.pathPhoto = path

        def getpathImg():
            return self.pathPhoto

        def setApelido(apelido):
            self.apelido = apelido

        def getApelido():
            return self.apelido

        def setCargo(cargo):
            self.cargo = cargo

        def getCargo():
            return self.cargo

        def countVotos():
            self.quantVotos += 1

        def getCount():
            return self.quantVotos
