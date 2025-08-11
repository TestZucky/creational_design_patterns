from factories.admin_factory import AdminFactory
from factories.customer_factory import CustomerFactory
from factories.base_factory import RoleFactory

def get_factory(user_role: str) -> RoleFactory:
    factories = {
        'admin': AdminFactory,
        'customer': CustomerFactory,
    }

    if user_role not in factories:
        raise ValueError(f"Invalid role: {user_role}")
    
    return factories[user_role]()
