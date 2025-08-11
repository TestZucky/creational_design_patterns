from abc import ABC, abstractmethod

class RoleFactory(ABC):

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def create_dashboard(self):
        pass
    
    @abstractmethod
    def create_notification(self):
        pass