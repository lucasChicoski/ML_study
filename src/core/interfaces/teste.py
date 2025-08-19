from abc import ABC, abstractmethod

class Teste(ABC):
    
    @abstractmethod
    def vai_de_teste(self):
        pass
    



class Animal(Teste):
    def x(self):
        return self
    
    def vai_de_teste(self):
        print('teste')
        pass
    
    



x = Animal()



print( x.x().vai_de_teste())