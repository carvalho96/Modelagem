from Candidato import Candidato
from Eleitor import Eleitor


class votacao:
    def __init__(self):
            self.candidatos = list()
            self.cargoint = 0
            self.listCargo = ["c1", "c2", "c3", "c4", "c5"]
            self.cargo = self.listCargo[self.cargoint]
            c = Candidato("Jorge0","0","4","0","0","c1")
            self.candidatos.append(c)
            a = Candidato("Jorge1","0","4","0","0","c2")
            self.candidatos.append(a)
            b = Candidato("Jorge2","0","4","0","0","c3")
            self.candidatos.append(b)
            d = Candidato("Jorge3","0","4","0","0","c4")
            self.candidatos.append(d)
            e = Candidato("Jorge4","0","4","0","0","c5")
            self.candidatos.append(e)
            b0 = Candidato("NULO","0","NULO","0","0","c1")
            self.candidatos.append(b0)
            b1 = Candidato("BRANCO","0","BRANCO","0","0","c1")
            self.candidatos.append(b1)
            b0 = Candidato("NULO","0","NULO","0","0","c2")
            self.candidatos.append(b0)
            b1 = Candidato("BRANCO","0","BRANCO","0","0","c2")
            self.candidatos.append(b1)
            b0 = Candidato("NULO","0","NULO","0","0","c3")
            self.candidatos.append(b0)
            b1 = Candidato("BRANCO","0","BRANCO","0","0","c3")
            self.candidatos.append(b1)
            b0 = Candidato("NULO","0","NULO","0","0","c4")
            self.candidatos.append(b0)
            b1 = Candidato("BRANCO","0","BRANCO","0","0","c4")
            self.candidatos.append(b1)
            b0 = Candidato("NULO","0","NULO","0","0","c5")
            self.candidatos.append(b0)
            b1 = Candidato("BRANCO","0","BRANCO","0","0","c5")
            self.candidatos.append(b1)
            self.eleitores = list()
            a1 = Eleitor("L", "1")
            a2 = Eleitor("L", "2")
            a3 = Eleitor("L", "3")
            a4 = Eleitor("L", "4")
            a5 = Eleitor("L", "5")
            self.eleitores.append(a1)
            self.eleitores.append(a2)
            self.eleitores.append(a3)
            self.eleitores.append(a4)
            self.eleitores.append(a5)
            self.horaInit = "SEI-LA"
            self.horaTermino = '23:16'

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
        for i in  range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo and self.candidatos[i].getNumero() == numero):
                self.candidatos[i].countVotos()
        c = Candidato("0","0","0","0","0","0")
        return c
        #procura e da ++
    def getCandidato(self, cargo, numero):
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo and self.candidatos[i].getNumero() == numero):
                return self.candidatos[i]
        c = Candidato("0","0","0","0","0","0")
        return c
        #procura candidato, retorna infos
    def sendData(self):
        print "La"
	#Brenno Implemente Aqui
    def getCarg(self):
        return self.cargo
    def plusC(self):
        self.cargoint += 1
        if (self.cargoint == 5):
		self.cargoint = 0
		self.cargo = self.listCargo[self.cargoint]
        	return 0
	self.cargo = self.listCargo[self.cargoint]
        return 1
    def Voted(self, x):
    	for i in  range(0 , len(self.eleitores)):
            if(self.eleitores[i].getCpf() == x):
                if(self.eleitores[i].getVoted() == 0):
                    self.eleitores[i].setVoted()
                    return 0
    	self.eleitores[i]
        return 1
