from Candidato import Candidato
from Eleitor import Eleitor

class votacao:
    def __init__(self):
        self.candidatos = []
        self.cargoint = 0
        self.listCargo = ["c1", "c2", "c3", "c4", "c5"]
        self.cargo = self.listCargo[self.cargoint]
        c = Candidato("Jorge","0","4","0","0","c1")
        self.candidatos.append(c)
        a = Candidato("Jo5rge","0","5","0","0","c2")
        self.candidatos.append(a)
        b = Candidato("Jorge","0","4","0","0","c3")
        self.candidatos.append(b)
        d = Candidato("Jorge","0","4","0","0","c4")
        self.candidatos.append(d)
        e = Candidato("Jorge","0","4","0","0","c5")
        self.candidatos.append(e)
        self.eleitores = []
        self.horaInit = "SEI-LA"
    def setHt(self,ht):
        self.horaTermino = ht
    def getHt(self):
        return self.horaTermino
    def UEvGet(self):
        print "La"
        #IMPLEMENTE AQUI JOVEM BRENNO
    def enviaResultados(self):
        print "La"
        #IMPLEMENTE AQUI JOVEM BRENNO
    def confirma(self, cargo, numero):
        for i in (0 , self.candidatos):
            if(self.candidatos[i].getCargo() == cargo and self.candidatos[i].getNumero() == numero):
                self.candidatos[i].countVotos()
        c = Candidato("0","0","0","0","0","0")
        return c
        #procura e da ++
    def getCandidato(self, cargo, numero):
        for i in (0 , self.candidatos):
            if(self.candidatos[i].getCargo() == cargo and self.candidatos[i].getNumero() == numero):
                return self.candidatos[i]
            c = Candidato("0","0","0","0","0","0")
            return c
        #procura candidato, retorna infos
    def sendData(self):
        print "La"
    def getCarg(self):
        return self.cargo
    def plusC(self):
        self.cargoint += 1
        self.cargo = self.listCargo[self.cargoint]
        if (self.cargoint == 6):
            return 0
        return 1
        #Brenno Implemente Aqui
