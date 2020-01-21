class Character:

    def __init__(self,nome,idade,jedi,vivo): #   Cria um personagem
        self.nome       =   nome
        self.idade      =   idade
        self.e_jedi     =   jedi
        self.vivo       =   vivo

    def isJedi(self):
        return self.e_jedi
        
    def isAlive(self):
        return self.vivo
        
    def Char_Kill(self):
        self.vivo   =   False
        
    def Char_Revive(self):
        self.vivo   =   True
        
    def Char_Quebrado(self):
        self.vivo   =   not(self.vivo)
        
    def Char_Details(self):
        aux =   self.nome+' is '+str(self.idade)+' years old'
        aux =   aux+'\n'
        
        if  self.isJedi()   :
            aux =   aux+self.nome+'is a Jedi'
        else    :
            aux =   aux+self.nome+' is not a Jedi'
        aux =   aux+'\n'
        
        if  self.isAlive()   :
            aux =   aux+self.nome+' is alive'
        else    :
            aux =   aux+self.nome+' is not alive D:'

        return  aux

def mensagem_bonita(char,quant):
    return  print(char*quant)

mensagem_bonita('*',48)
luke = Character("Luke Skywalker",21,True,True)
print(luke.Char_Details())

mensagem_bonita('*',48)
leia = Character("Leia Skywalker",21,False,True)
leia.Char_Quebrado()
leia.Char_Quebrado()
print(leia.Char_Details())

mensagem_bonita('*',48)  
han = Character("Han Solo",26,False,False)
print(han.Char_Details())