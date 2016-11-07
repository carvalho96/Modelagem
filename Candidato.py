from Pessoa import pessoa

class Candidato(pessoa):
        def __init__(self, nome, cpf, numero, pathPhoto, Apelido, Cargo):
            pessoa.__init__(self, nome, "0")
            #super(Candidato, self).__init__(nome, cpf)
            self.numero = numero
            self.quantVotos = 0
            self.pathPhoto = pathPhoto
            self.apelido = "0"
            self.cargo = Cargo

        def setNumero(self, numero):
            self.numero = numero

        def getNumero(self):
            return self.numero

        def setpathImg(self, path):
            self.pathPhoto = path

        def getpathImg(self):
            return self.pathPhoto

        def setApelido(self, apelido):
            self.apelido = apelido

        def getApelido(self):
            return self.apelido

        def setCargo(self, cargo):
            self.cargo = cargo

        def getCargo(self):
            return self.cargo

        def countVotos(self):
            self.quantVotos += 1

        def getCount(self):
            return self.quantVotos
