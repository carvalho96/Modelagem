from Candidato import Candidato
from Eleitor import Eleitor


class votacao:
    def __init__(self):
            self.candidatos = list()
            self.eleitores = list()
            self.listCargo = []
            self.cargoint = 0
            self.cargo = str()
            self.horaInit = "SEI-LA"
            self.horaTermino = '20:25'

    def setHt(self,ht):
        self.horaTermino = ht
    def getHt(self):
        return self.horaTermino
    def UEvGet(self):
        self.listCargo = ["vereador", "prefeito", "presidente", "governador", "deputado"]
        self.cargo = self.listCargo[self.cargoint]
        c = Candidato("James","0","1002","0","0","vereador")
        self.candidatos.append(c)
        a = Candidato("Mary","0","1006","0","0","vereador")
        self.candidatos.append(a)
        b = Candidato("Charlie","0","1010","0","0","vereador")
        self.candidatos.append(b)
        d = Candidato("Cris","0","1014","0","0","vereador")
        self.candidatos.append(d)
        e = Candidato("BRANCO","0","BRANCO","0","0","vereador")
        self.candidatos.append(e)
        b0 = Candidato("NULO","0","NULO","0","0","vereador")
        self.candidatos.append(b0)

        c = Candidato("Beth","0","1060","0","0","deputado")
        self.candidatos.append(c)
        a = Candidato("Lisa","0","1020","0","0","deputado")
        self.candidatos.append(a)
        e = Candidato("BRANCO","0","BRANCO","0","0","deputado")
        self.candidatos.append(e)
        b0 = Candidato("NULO","0","NULO","0","0","deputado")
        self.candidatos.append(b0)

        c = Candidato("Pow","0","100002","0","0","prefeito")
        self.candidatos.append(c)
        a = Candidato("Jeny","0","100006","0","0","prefeito")
        self.candidatos.append(a)
        e = Candidato("BRANCO","0","BRANCO","0","0","prefeito")
        self.candidatos.append(e)
        b0 = Candidato("NULO","0","NULO","0","0","prefeito")
        self.candidatos.append(b0)

        c = Candidato("Susan","0","12","0","0","governador")
        self.candidatos.append(c)
        a = Candidato("Bryan","0","16","0","0","governador")
        self.candidatos.append(a)
        e = Candidato("BRANCO","0","BRANCO","0","0","governador")
        self.candidatos.append(e)
        b0 = Candidato("NULO","0","NULO","0","0","governador")
        self.candidatos.append(b0)

        c = Candidato("Gary","0","10002","0","0","presidente")
        self.candidatos.append(c)
        a = Candidato("Tim","0","10003","0","0","presidente")
        self.candidatos.append(a)
        e = Candidato("BRANCO","0","BRANCO","0","0","presidente")
        self.candidatos.append(e)
        b0 = Candidato("NULO","0","NULO","0","0","presidente")
        self.candidatos.append(b0)

        a1 = Eleitor("James", "1")
        a2 = Eleitor("Mary", "2")
        a3 = Eleitor("Charlie", "3")
        a4 = Eleitor("Cris", "4")
        a5 = Eleitor("Pow", "5")
        self.eleitores.append(a1)
        self.eleitores.append(a2)
        self.eleitores.append(a3)
        self.eleitores.append(a4)
        self.eleitores.append(a5)

        a1 = Eleitor("Jenny", "6")
        a2 = Eleitor("Susan", "7")
        a3 = Eleitor("Bryan", "8")
        a4 = Eleitor("Lisa", "9")
        a5 = Eleitor("Betty", "10")
        self.eleitores.append(a1)
        self.eleitores.append(a2)
        self.eleitores.append(a3)
        self.eleitores.append(a4)
        self.eleitores.append(a5)
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
        if (self.cargoint == len(self.listCargo) ):
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
        return 1
    def printaResultados(self):
        print "-----------------------RESULTADOS--------------------------"
        cargo = "vereador"
        print cargo
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo):
                print "Nome: ", self.candidatos[i].getNome()
                print "Votos: ", self.candidatos[i].getCount()
        print "-----------------------RESULTADOS--------------------------"
        cargo = "prefeito"
        print cargo
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo):
                print "Nome: ", self.candidatos[i].getNome()
                print "Votos: ", self.candidatos[i].getCount()
        print "-----------------------RESULTADOS--------------------------"
        cargo = "presidente"
        print cargo
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo):
                print "Nome: ", self.candidatos[i].getNome()
                print "Votos: ", self.candidatos[i].getCount()
        print "-----------------------RESULTADOS--------------------------"
        cargo = "governador"
        print cargo
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo):
                print "Nome: ", self.candidatos[i].getNome()
                print "Votos: ", self.candidatos[i].getCount()
        print "-----------------------RESULTADOS--------------------------"
        cargo = "deputado"
        print cargo
        for i in range(0 , len(self.candidatos)):
	    if(self.candidatos[i].getCargo() == cargo):
                print "Nome: ", self.candidatos[i].getNome()
                print "Votos: ", self.candidatos[i].getCount()
        print "-----------------------------------------------------------"
