from abc import ABC, abstractmethod

class BaseAbstractClass(ABC):
    
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def update_datos(self):
        pass