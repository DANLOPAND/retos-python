# Base de datos simulada de usuarios y sus niveles de acceso
users_db = {
    "user1": {"password": "123", "level": "usuario"},
    "user2": {"password": "456", "level": "administrador"},
    "user3": {"password": "789", "level": "superusuario"}
}

# Decorador para verificar la autenticación y nivel mínimo de acceso
def auth_required(min_level):
    def decorator(func):
        def wrapper(username, password, *args, **kwargs):
            user = users_db.get(username)
            # Verificar si el usuario y la contraseña coinciden y si el nivel es válido
            if user and user["password"] == password and user["level"] in ["superusuario", "administrador", "usuario"]:
                # Comprobar los permisos basados en la jerarquía de niveles
                if user["level"] == "superusuario" or (user["level"] == "administrador" and min_level != "superusuario") or (user["level"] == "usuario" and min_level == "usuario"):
                    return func(username, *args, **kwargs)
                else:
                    return f"No tienes permiso para acceder a esta función."
            else:
                return f"Usuario o contraseña incorrectos."
        return wrapper
    return decorator

# Funciones decoradas con diferentes niveles de acceso requeridos
@auth_required("superusuario")
def superuser_function(username):
    return f"Función de solo los superusuarios puden ejecutar esto: {username}."


@auth_required("administrador")
def admin_function(username):
    return f"Función de admnistradores y superusuarios puden ejecutar esto: {username}."

@auth_required("usuario")
def user_function(username):
    return f"todos pueden ejecuarlo: {username}."

print("                              ")
print(superuser_function("user1", "123"))
print(superuser_function("user2", "456"))
print(superuser_function("user3", "789"))
print("                              ")
print(admin_function("user1", "123"))
print(admin_function("user2", "456"))
print(admin_function("user3", "789"))
print("                              ")
print(user_function("user1", "123"))
print(user_function("user2", "456"))
print(user_function("user3", "789"))
print("                              ")
