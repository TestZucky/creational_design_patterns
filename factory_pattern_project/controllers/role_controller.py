from utils.factory_provider import get_factory

def handle_role(user_role: str):
    factory = get_factory(user_role)
    
    user = factory.create_user()
    dashboard = factory.create_dashboard()
    notification = factory.create_notification()

    user.create_user()
    dashboard.create_dashboard()
    notification.create_notification()
