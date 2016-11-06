import Candidato
import Eleitor

class Votacao:
    def __init__(self):
        self.candidatos = []
        self.eleitores = []
        self.horaInit = "SEI-LA"
    def setHt(ht):
        self.horaTermino = ht
    def getHt():
        return self.horaTermino
    def UEvGet():
        print "La"
        #IMPLEMENTE AQUI JOVEM BRENNO
    def enviaResultados():
        print "La"
        #IMPLEMENTE AQUI JOVEM BRENNO
    def confirma(cargo, numero):
        for i in (0 , len(self.candidatos)):
            if(self.candidatos[i].getCargo == cargo and self.candidatos[i].getNumero == numero):
                self.candidatos[i].countVotos

        #procura e da ++
    def getCandidato(cargo, numero):
        for i in (0 , len(self.candidatos)):
            if(self.candidatos[i].getCargo == cargo and self.candidatos[i].getNumero == numero):
                return self.candidatos[i]
        #procura candidato, retorna infos
    def sendData():
        print "La"
        #Brenno Implemente Aqui
