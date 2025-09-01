import random
"""
Login verfication and Roles demonstration
Here we are defining the class of Users and Admins
"""
class User:
    user_registry = []

    def __init__(self, first_name, last_name, age, email, password, role = "User"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.role = role
        User.user_registry.append(self)

    def remove(self):
        User.user_registry.remove(self)

class Admin:
    admin_registry = []

    def __init__(self, first_name, last_name, age, email, password, role = "Admin"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.role = role
        Admin.admin_registry.append(self)

    def remove(self):
        Admin.admin_registry.remove(self)

"""
Next we are gonna define a function to determine if a given email is a valid email,
while also calling upon the correct class type to attach to the person logging in.
We then want to hold that user name (the variable name used to create the object)
to check a password against that same user's password for verification.
We also have an example of a user and an admin
"""
temp_user_name = None

def Validation_Email(given_email):
    for user in User.user_registry:
        if user.email == given_email:
            login_status = "Valid"
            return login_status
    for admin in Admin.admin_registry:
        if admin.email == given_email:
            login_status = "Valid"
            return login_status
    print("This email is not found in our database")
    return

def Validation_Password(given_password, given_email): #This one is for validating a password that was already created
    for user in User.user_registry:
        if user.email == given_email and user.password == given_password:
            login_status = "Valid User"
            return login_status
    for admin in Admin.admin_registry:
        if admin.email == given_email and admin.password == given_password:
            login_status = "Valid User"
            return login_status
    print("This password does not match this email.")
    login_status = "Valid"
    return login_status

def verify_password(password): #This is for verifying that a password being created follows password creation rules
    special_chars = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/`~"

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(c.isupper() for c in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(c.islower() for c in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(c.isdigit() for c in password):
        print("Password must contain at least one number.")
    elif not any(c in special_chars for c in password):
        print("Password must contain at least one special character.")
    else:
        return True
    return False

login_status = None
new_user = User("Tery", "Jones", 27, "terydaman@email.com", "TeryDaMan123") #Oh Tery, you are just asking to be hacked with a password like that.
new_admin = Admin("Helen", "Laurence", 45, "hlaurence45@email.com", "G4rf23!:hHr9t6")

def New_User(first_name, last_name, age, email, password):
    new_user = User(first_name, last_name, age, email, password)
    print("New user created. Please return to log in screen. ")
    return new_user

def Promote_User(given_email):
    for admin in Admin.admin_registry:
        if admin.email == given_email:
            print("This person is already an admin.")
            return None

    for user in User.user_registry:
        if user.email == given_email:
            new_admin = Admin(user.first_name, user.last_name, user.age, user.email, user.password)
            print(f"User {user.first_name} {user.last_name} has been promoted to the admin role.")
            user.remove()
            return new_admin

    print("This user does not exist in our database. Please try again.")
"""
Now that we have a way to create users, promote users, and validate the information of users, let's actually log them in.
"""
Login = True
Lockout = False
Counter = 0
X = True
Y = True

while Login is True:
    Question = input('Are you looking to sign in or sign up? ')
    Question = Question.upper()
    if Question == "SIGN IN":
        while Login is True and Lockout is False:
            given_email = input("Please enter your email ")
            login_status = Validation_Email(given_email)
            if login_status == "Valid":
                given_password = input("Please enter you password ")
                login_status = Validation_Password(given_password, given_email)
                if login_status == "Valid":
                    Counter += 1
                    if Counter == 3:
                        print("The account has been locked due to too many failed login attempts. Please contact admin level member to unlock your account.")
                        Lockout = True
                    else:
                        print("Please try again. the system will lock after too many consecutive failed attempts.")
                else:
                    print("Excellent!!! You are logged in.")
                    Login = False
    elif Question == "SIGN UP":
        print("I will gladly help you sign up.")
        first_name = input("Please tell me your first name. ")
        last_name = input("Please tell me your last name. ")
        age = input("Please tell me how old you are. ")

        while True:
            email = input("Please provide a valid email address: ")
            if "@" not in email or ".com" not in email:
                print("That is not a valid email.")
            else:
                break

        while Y is True:
            print("Please create a password following these rules. ")
            print()
            print("Your password must be eight characters long")
            print("Your password much contain upper and lower case letters")
            print("Your password must contain numbers")
            password = input("Your password must contain at least one special character ")
            result = verify_password(password)
            if result is True:
                Y = False

        print()
        print("Congrats!!! You are now officially a user!!!")
        login_status = "Valid User"
        Login = False
    else:
        print("That is not a valid option.")

"""
Now that they can log in. Let's creature some functions for them to use.
"""
def Check_Hours():
    Time = random.randint (1, 40)
    return Time

def Check_Schedule():
    Days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    Schedule = random.sample(Days_of_week, 5)
    return Schedule

def Request_Admin_Status():
    print("I'm not a valid admin to grant such a thing")
    return None

def Request_Time_Off():
    if login_status == "Valid User":
        print("Again? You took time off last year. Need you do it again?")
    elif login_status == "Valid Admin":
        print("Right away sir/madam. I will put that in for you.")

    return None

def Remove_User():
    Name = input("What is the first name of the user? ")

    for user in User.user_registry:
        if user.first_name == Name:
            user.remove()
            return None

    print("The pest has been removed.")

"""
And finally a menu to use the functions.
"""
while True:
    options = ["[1] Check your timecard", "[2] Check your schedule", "[3] Request time off", "[4] Request Admin Status", "[5] Promote a User", "[6] Remove a User", "[7] Logout"]
    for option in options:
        print(option)

    selection = input("Please select an option.")
    if selection == "1":
        Time = Check_Hours()
        print(f"You have worked a total of {Time} hours this pay peroid")
        print()
    elif selection == "2":
        print("You work the following days this week")
        print(Check_Schedule())
        print()
    elif selection == "3":
        Request_Time_Off()
        print()
    elif selection == "4":
        if login_status == "Valid User":
            Request_Admin_Status()
            print()
        else:
            print("I can not give you what you already are.")
            print()
    elif selection == "5":
        if login_status == "Valid User":
            print("You are not authorized to use this function.")
            print()
        else:
            given_email = input("What is the email of the user you want to promote? ")
            Promote_User(given_email)
            print()
    elif selection == "6":
        if login_status == "Valid User":
            print("You are not authorized to use this function.")
            print()
        else:
            Remove_User()
            print()
    elif selection == "7":
        print("Have a good day!!!")
        exit()
    else:
        print("That is not a valid option.")

        print()

