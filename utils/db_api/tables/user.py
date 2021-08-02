from types_1.user import UserRole
from utils.db_api.db import execute


class User:
    def __init__(self, id: int, username: str, fullname: str, role: str = UserRole.USER, cash: int = 0):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.role = role
        self.cash = cash
        if not User.is_user(self.id):
            execute(f"INSERT INTO users (id, username, fullname, role, cash) VALUES (?, ?, ?, ?, ?)",
                    (self.id, self.username, self.fullname, self.role, self.cash))
            print('Добавлен новый пользователь')

    def __repr__(self):
        return f'User id: {self.id}\nUsername: @{self.username}\n' \
               f'Fullname: {self.fullname}\nRole: {self.role}\nCash: {self.cash}'

    def update(self, **kwargs):
        """
        Функция обновляет данныне о пользователе в базе
        """
        for key, value in kwargs.items():
            execute(f"UPDATE users SET {key} = {value} WHERE id = {self.id}")

    @staticmethod
    def is_user(user_id):
        """
        Фенкция проверяет налчие пользователя в базе данных
        """
        return execute(f"SELECT * FROM users WHERE id = {user_id}")

    @staticmethod
    def get_user(user_id):
        """
        Функция возвращает данные о пользователе в виде класса
        """
        id, username, fullname, role, cash = execute(f"SELECT * FROM users WHERE id = {user_id}")[0]
        return User(id, username, fullname, role, cash)

    @staticmethod
    def get_users():
        """
        Функция возвращает список пользователей в виде классов
        """
        users = []
        for user in execute("SELECT * FROM users"):
            id, username, fullname, role, cash = user
            user = User(id, username, fullname, role, cash)
            users.append(user)
        return users

    @staticmethod
    def get_cash(user_id):
        """
        Функция возвращает баланс пользователя
        """
        return execute(f"SELECT cash FROM users WHERE id = {user_id}")[0][0]

    @staticmethod
    def cash_up(user_id, money: int):
        """
        Функция увеличивает баланс пользователя
        """
        balance = User.get_cash(user_id)
        execute(f"UPDATE users SET cash = {balance + money} WHERE id = {user_id}")

    @staticmethod
    def cash_down(user_id, money: int):
        """
        Функция уменьшает баланс пользователя
        """
        balance = User.get_cash(user_id)
        # Проверка на отрицательный баланс
        if balance - money <= 0:
            execute(f"UPDATE users SET cash = {0} WHERE id = {user_id}")
        else:
            execute(f"UPDATE users SET cash = {balance - money} WHERE id = {user_id}")
