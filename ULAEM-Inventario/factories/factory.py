from abc import ABC, abstractmethod

class Factory(ABC):
    
    @abstractmethod
    def crear_objeto(self, datos):
        pass