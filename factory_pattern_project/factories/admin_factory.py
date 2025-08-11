from factories.base_factory import RoleFactory
from products.users import AdminUser
from products.dashboards import AdminDashboard
from products.notifications import AdminNotification

class AdminFactory(RoleFactory):

    def create_user(self):
        return AdminUser()
    
    def create_dashboard(self):
        return AdminDashboard()
    
    def create_notification(self):
        return AdminNotification()
