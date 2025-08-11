from controllers.role_controller import handle_role

if __name__ == "__main__":
    role = "admin"   # Could come from request, DB, etc.
    handle_role(role)
