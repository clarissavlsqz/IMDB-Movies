import db
from adapters.models import User

def welcome_message(new_user : User) -> int:
    print("Bienvenido al servicio de Flix\nPara utilizar nuestro servicio debes de estar registrado con nosotros\nSeleccione el método con el que se identifique")
    print("1. Usuario registrado\n2. Usario nuevo\n[1 o 2]")
    choice = input()
    while choice != 1 or choice != 2:
        print("Selección ingresada incorrecta, intente de nuevo")
        print("1. Usuario registrado\n2. Usario nuevo\n[1 o 2]")
        choice = input()
   
    if choice == 1:
        user_username = input("Ingrese su usuario: ")
        user_email = input("Ingrese su correo electrónico: ")
        if verify_user_is_registered(user_username, user_email):
            user_preference_key = db.session.query(User.preference_key).filter(User.username == new_user.username, User.email == new_user.email).first()
            return user_preference_key
        else:
            print("Usuario no registrado")
    else:
        register_user(new_user)
        return new_user.preference_key

def register_user(new_user : User) -> None:
    user_username = input("Ingrese el nombre de usuario que utilizará para ingresar sesión en Flix: ")
    while username_exists_in_db(user_username):
        user_username = input("El nombre de usuario ya existe, ingrese otro: ")

    new_user.set_username(user_username)

    user_email = input("Ingrese un correo electrónico válido para ingresar sesión en Flix: ")
    while email_exists_in_db(user_email):
        user_email = input("El correo electrónico ya se utilizó para registrar a un usuario, intente otro: ")
 
    while new_user.set_email(user_email) == False:
        user_email = input("El formato del correo electrónico es incorrecto (user@domain.com), intente de nuevo")

    getGenres()

    first_genre = input("Ingrese el número de uno de los géneros que guste [1-5]: ")
    second_genre = input("Ingrese el número de uno de los géneros que guste [1-5]: ")
    third_genre = input("Ingrese el número de uno de los géneros que guste [1-5]: ")

    preference_key = calculate_preference(first_genre, second_genre, third_genre)

    new_user.set_preference_key(preference_key)

    db.session.add(new_user)
    db.session.commit()

    print("¡Usuario registrado exitosamente!")

def getGenres() -> None:
    print("Seleccione sus tres genéros favoritos: ")
    print("1. Comedia\n2. Drama\n3. Sci-Fi\n4. Romantico\n5. Aventura")

def calculate_preference(genre_1 : int, genre_2 : int, genre_3 : int) -> int:
    return ((genre_1 * genre_2 * genre_3) % 5) + 1

def username_exists_in_db(username : str) -> bool:
    username_db = db.session.query(User).filter(User.username == username).first()
    if username_db is not None:
        return True
    else:
        return False

def email_exists_in_db(email : str) -> bool:
    email_db = db.session.query(User).filter(User.email == email).first()
    if email_db is not None:
        return True
    else:
        return False

def verify_user_is_registered(username : str, email : str) -> bool:
    registered_user = db.session.query(User).filter(User.username == username, User.email == email).first()
    if registered_user is not None:
        return True
    else:
        return False

def getPreferenceKey(username : str, email : str) -> int:
    pref_key = db.session.query(User.preference_key).filter(User.username == username, User.email == email).first()
    return pref_key