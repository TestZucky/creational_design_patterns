from factories.base_factory import RoleFactory
from products.users import CustomerUser
from products.dashboards import CustomerDashboard
from products.notifications import CustomerNotification

class CustomerFactory(RoleFactory):

    def create_user(self):
        return CustomerUser()
    
    def create_dashboard(self):
        return CustomerDashboard()
    
    def create_notification(self):
        return CustomerNotification()
