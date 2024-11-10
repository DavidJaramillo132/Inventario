from abc import ABC, abstractmethod

# Interfaz de Observer
class Observer(ABC):
    @abstractmethod
    def update(self, event_type, data):
        pass

# Clase de Sujeto
class Subject:
    def __init__(self):
        self._observers = []
        self._items = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)
        self.notify_observers("observer_added", observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
        self.notify_observers("observer_removed", observer)

    def add_item(self, item):
        self._items.append(item)
        self.notify_observers("item_added", item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            self.notify_observers("item_removed", item)

    def notify_observers(self, event_type, data):
        for observer in self._observers:
            observer.update(event_type, data)

# Implementación de observadores concretos
class ConcreteObserver(Observer):
    def update(self, event_type, data):
        print(f"Observer recibió evento '{event_type}' con datos: {data}")

# Uso del patrón Observer con eventos específicos
if __name__ == "__main__":
    # Crear el sujeto
    subject = Subject()

    # Crear observador
    observer = ConcreteObserver()

    # Añadir observador al sujeto
    subject.add_observer(observer)

    # Agregar y eliminar elementos, notificando a los observadores
    subject.add_item("Elemento 1")
    subject.add_item("Elemento 2")
    subject.remove_item("Elemento 1")

    # Eliminar observador
    subject.remove_observer(observer)
