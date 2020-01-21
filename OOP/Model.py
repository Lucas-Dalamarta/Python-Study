class Character:

    def __init__(self,nome,idade,jedi):
        self.nome       =   nome
        self.idade      =   idade
        self.e_jedi     =   jedi

    def isJedi(self):
        return self.e_jedi

luke = Character("Luke Skywalker",21,True)

print(luke.nome+' is '+str(luke.idade)+' years old')
if luke.isJedi()    :
    print(luke.nome+' is a Jedi')
else    :
    print(luke.nome+' is not a Jedi')