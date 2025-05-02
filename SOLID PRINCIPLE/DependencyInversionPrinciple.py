# "High-level modules should not depend on low-level modules directly."
# class MySqlDB:

#     def connect(self):
#         print("Connecting to MySqlDB")

# class App:
#     def __init__(self):
#         self.db = MySqlDB()
    
#     def start(self):
#         self.db.connect()

# app = App()
# app.start()


# Problem:
# App is tightly coupled with MySQL.


from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySqlDB(Database):
    def connect(self):
        print(f"Connected to {self.__class__.__name__}")

class PostgresqlDB(Database):
    def connect(self):
        print(f"Connected to {self.__class__.__name__}")

class App:
    def __init__(self, database: Database):
        self.db = database

    def start(self):
        self.db.connect()

mysql = MySqlDB()
postgre = PostgresqlDB()
sql = App(mysql)
sql.start()
post = App(postgre)
post.start()

        