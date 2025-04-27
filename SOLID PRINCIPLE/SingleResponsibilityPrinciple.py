# "One class = one responsibility. Not more!"

#bad example

class User:
    def __init__(self,name):
        self.name = name

    def save_to_db(self):
        print(f"{self.name} saved to db")

    def send_email(self):
        print(f"sent email to {self.name}")

#here class User is having to many responsibility as it is interacting with db
#as well as it is also sending mail to user.

# manish = User("manish")
# manish.save_to_db()
# manish.send_email()


#good example
class User:
    def __init__(self, name):
        self.name = name

class DB:
    def __init__(self, user):
        self.user = user
    
    def save_to_db(self):
        print(f"{self.user.name} saved to db")

class Email:
    def __init__(self, user):
        self.user = user

    def send_email(self):
        print(f"email sent to {self.user.name}")

manish = User("manish")
save_data = DB(manish)
save_data.save_to_db()

send_mail = Email(manish)
send_mail.send_email()

#Separate classes = one responsibility each.